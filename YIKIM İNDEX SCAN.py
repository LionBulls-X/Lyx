import os
import re
import time
import sqlite3
import requests
import asyncio
import aiohttp
import aiofiles
from urllib.parse import urljoin, urlparse, urldefrag
from bs4 import BeautifulSoup
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from urllib.robotparser import RobotFileParser
from termcolor import colored
import pyfiglet
from colorama import Fore, Style, init
from time import sleep

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
DB_FILE = "index_tool.db"
INDEX_DIR = "indexdir"
REQUEST_TIMEOUT = 8
RATE_LIMIT_SECONDS = 0.5
MAX_PAGES_DEFAULT = 200
VULN_LOG_FILE = "vuln_report.txt"

COMMON_FILES = [
    # Admin ve yönetim panelleri
    "/admin", "/wp-admin", "/login", "/administrator", "/manager", "/dashboard",
    "/controlpanel", "/webadmin", "/admincp", "/admin_login", "/adminarea",
    "/useradmin", "/sysadmin", "/admin1", "/admin2", "/admin3", "/admin4",
    "/admin5", "/siteadmin", "/server-admin", "/cpanel", "/whm", "/plesk",
    
    # Giriş sayfaları
    "/login", "/log-in", "/signin", "/sign-in", "/auth", "/authentication",
    "/memberlogin", "/userlogin", "/stafflogin", "/admin-login", "/wp-login.php",
    "/login.php", "/signin.php", "/auth.php", "/securelogin", "/secure-login",
    
    # Yapılandırma dosyaları
    "/config", "/configuration", "/config.php", "/config.json", "/config.xml",
    "/config.yml", "/config.yaml", "/config.ini", "/config.bak", "/config.old",
    "/config.txt", "/config.php.bak", "/config.php.old", "/config.php.save",
    "/config.php~", "/config.php.swp", "/config.php.orig", "/config.php.dist",
    "/config.php.backup", "/config.php.bkp", "/config.php.tmp", "/config.php.temp",
    "/config.php.default", "/config.sample.php", "/config.inc.php",
    "/configuration.php", "/settings.php", "/settings.inc.php", "/app.config",
    "/web.config", "/application.config", "/database.config", "/db.config",
    
    # Environment dosyaları
    "/.env", "/.env.local", "/.env.dev", "/.env.development", "/.env.prod",
    "/.env.production", "/.env.staging", "/.env.test", "/.env.example",
    "/.env.sample", "/.env.backup", "/.env.old", "/.env.bak", "/env", "/env.php",
    "/environment", "/environment.php",
    
    # Backup dosyaları
    "/backup", "/backups", "/backup.sql", "/db.sql", "/database.sql",
    "/backup.zip", "/backup.tar", "/backup.tar.gz", "/backup.rar",
    "/backup.db", "/backup.mdb", "/backup.accdb", "/backup.bak",
    "/backup.tgz", "/backup.7z", "/backup.old", "/backup.new",
    "/backup_old", "/backup_new", "/backup-latest", "/backup-current",
    "/full-backup", "/incremental-backup", "/daily-backup", "/weekly-backup",
    "/monthly-backup", "/yearly-backup", "/backup-2023", "/backup-2024",
    
    # Database dosyaları
    "/db", "/database", "/db.sql", "/database.sql", "/db.sqlite", "/database.sqlite",
    "/db.db", "/database.db", "/db.mdb", "/database.mdb", "/db.accdb",
    "/database.accdb", "/db.dump", "/database.dump", "/db.backup",
    "/database.backup", "/db.bak", "/database.bak", "/db.old", "/database.old",
    "/db.tar", "/database.tar", "/db.tar.gz", "/database.tar.gz",
    "/db.zip", "/database.zip",
    
    # Git ve version control
    "/.git", "/.gitignore", "/.gitconfig", "/.git-credentials", "/.gitmodules",
    "/.git/HEAD", "/.git/logs/HEAD", "/.git/config", "/.git/description",
    "/.git/hooks", "/.git/index", "/.git/info", "/.git/objects",
    "/.git/refs", "/.git/refs/heads", "/.git/refs/tags", "/.svn", "/.hg",
    "/.bzr", "/.cvs",
    
    # IDE ve editor dosyaları
    "/.idea", "/.vscode", "/.vs", "/.project", "/.classpath", "/.settings",
    "/.buildpath", "/.factorypath", "/.tmproj", "/.nbattrs",
    
    # Log dosyaları
    "/logs", "/log", "/error.log", "/access.log", "/error_log", "/access_log",
    "/apache.log", "/nginx.log", "/iis.log", "/server.log", "/debug.log",
    "/app.log", "/application.log", "/system.log", "/security.log",
    "/audit.log", "/trace.log", "/php_errors.log", "/mysql.log",
    "/database.log", "/db.log",
    
    # PHP info ve test dosyaları
    "/phpinfo.php", "/info.php", "/test.php", "/debug.php", "/php-info.php",
    "/php_info.php", "/phpinfo", "/info", "/test", "/debug",
    
    # Server status ve monitoring
    "/server-status", "/server-info", "/server-health", "/status", "/health",
    "/monitoring", "/metrics", "/stats", "/statistics", "/server-stats",
    
    # Web server yapılandırmaları
    "/.htaccess", "/.htpasswd", "/web.config", "/httpd.conf", "/nginx.conf",
    "/apache2.conf", "/.user.ini", "/php.ini", "/my.ini", "/my.cnf",
    
    # SSL ve sertifika dosyaları
    "/.crt", "/.pem", "/.key", "/.cer", "/.pfx", "/ssl", "/cert", "/certs",
    "/certificate", "/certificates",
    
    # Framework spesifik dosyalar
    "/composer.json", "/composer.lock", "/package.json", "/package-lock.json",
    "/yarn.lock", "/Gemfile", "/Gemfile.lock", "/pom.xml", "/build.xml",
    "/Makefile", "/Dockerfile", "/docker-compose.yml",
    
    # CMS spesifik dosyalar (WordPress)
    "/wp-config.php", "/wp-config.php.bak", "/wp-config.php.old",
    "/wp-config.php.save", "/wp-config.php~", "/wp-config.php.swp",
    "/wp-config.php.orig", "/wp-config.php.backup", "/wp-content",
    "/wp-includes", "/xmlrpc.php", "/wp-cron.php", "/wp-mail.php",
    "/wp-signup.php", "/wp-trackback.php", "/wp-comments-post.php",
    
    # CMS spesifik (Joomla)
    "/configuration.php", "/configuration.php.bak", "/configuration.php.old",
    "/configuration.php.save", "/configuration.php.backup",
    
    # CMS spesifik (Drupal)
    "/sites/default/settings.php", "/sites/default/default.settings.php",
    
    # Diğer framework ve CMS'ler
    "/app/etc/local.xml", # Magento
    "/application/config/database.php", # CodeIgniter
    "/app/config/parameters.yml", # Symfony
    "/.env.production.local", # Laravel
    "/.env.local.php", # Laravel
    
    # API endpoint'leri
    "/api", "/api/v1", "/api/v2", "/graphql", "/rest", "/soap", "/json",
    "/xml", "/rpc", "/webhook", "/webhooks", "/callback", "/callbacks",
    
    # File upload ve media
    "/uploads", "/upload", "/files", "/file", "/images", "/image", "/media",
    "/assets", "/static", "/public", "/download", "/downloads",
    
    # Temporary ve cache dosyaları
    "/tmp", "/temp", "/cache", "/caches", "/session", "/sessions",
    "/tempory", "/temporaries",
    
    # Shell ve backdoor olasılıkları
    "/shell.php", "/cmd.php", "/c99.php", "/r57.php", "/wso.php", "/b374k.php",
    "/adminer.php", "/phpmyadmin.php", "/sql.php", "/mysql.php",
    "/x.php", "/0x.php", "/antichat.php", "/cybershell.php",
    
    # Database management
    "/phpmyadmin", "/adminer", "/mysql-admin", "/dbadmin", "/pma", "/myadmin",
    "/sqlite", "/sqlitemanager", "/db-admin", "/database-admin",
    
    # File manager
    "/filemanager", "/filesman", "/fm", "/file-manager", "/explorer",
    "/browser", "/finder",
    
    # Eski ve yedek dosya uzantıları
    ".bak", ".backup", ".old", ".save", ".sav", ".tmp", ".temp", ".copy",
    ".orig", ".original", ".new", ".dist", ".example", ".sample", ".demo",
    ".test", ".testing", ".dev", ".development", ".staging", ".prod",
    ".production", ".live", ".public", ".private", ".local", ".remote",
    
    # Compressed dosyalar
    ".zip", ".tar", ".gz", ".tgz", ".rar", ".7z", ".bz2", ".xz",
    
    # Database dump uzantıları
    ".sql", ".dump", ".db", ".mdb", ".accdb", ".sqlite", ".sqlite3",
    ".dbf", ".mdf", ".ndf", ".ldf",
    
    # Log file uzantıları
    ".log", ".txt", ".out", ".err",
    
    # Configuration file uzantıları
    ".cfg", ".conf", ".config", ".ini", ".inf", ".properties", ".prop",
    ".yml", ".yaml", ".xml", ".json",
    
    # Certificate file uzantıları
    ".crt", ".pem", ".key", ".cer", ".der", ".pfx", ".p12", ".csr",
    
    # Backup specific patterns
    "_backup", "-backup", ".back", "_old", "-old", ".previous", "_prev",
    "-prev", ".archive", "_archive", "-archive",
    
    # Versioned files
    ".v1", ".v2", ".v3", "_v1", "_v2", "_v3", "-v1", "-v2", "-v3",
    ".1", ".2", ".3", "_1", "_2", "_3", "-1", "-2", "-3",
    
    # Date stamped backups
    ".2023", ".2024", ".2025", "_2023", "_2024", "_2025",
    "-2023", "-2024", "-2025", ".2301", ".2401",
    
    # IDE specific
    ".swp", ".swo", ".swn", ".un~", ".todo", ".project", ".classpath",
    
    # OS specific
    ".DS_Store", "Thumbs.db", ".Spotlight-V100", ".Trashes",
    
    # Development tools
    ".map", ".min.js", ".min.css", ".bundle.js", ".chunk.js",
    
    # Additional security testing paths
    "/.well-known", "/.well-known/security.txt", "/robots.txt", "/sitemap.xml",
    "/crossdomain.xml", "/clientaccesspolicy.xml", "/security.txt",
    "/humans.txt", "/ads.txt", "/.gitignore", "/README", "/README.md",
    "/CHANGELOG", "/CHANGELOG.md", "/LICENSE", "/LICENSE.txt",
    "/CONTRIBUTING.md", "/SECURITY.md",
    
    # Authentication related
    "/oauth", "/oauth2", "/openid", "/saml", "/cas", "/auth", "/.auth",
    "/_auth", "/secure", "/.secure", "/_secure", "/private", "/.private",
    "/_private", "/protected", "/.protected", "/_protected",
    
    # System directories
    "/bin", "/sbin", "/usr", "/etc", "/var", "/opt", "/lib", "/lib64",
    "/sys", "/proc", "/dev", "/mnt", "/media", "/home", "/root",
    
    # Web services
    "/services", "/webservices", "/web-services", "/api-docs", "/swagger",
    "/swagger-ui", "/redoc", "/api-explorer",
    
    # Development and testing
    "/dev", "/development", "/test", "/testing", "/stage", "/staging",
    "/demo", "/demonstration", "/sandbox", "/playground",
    
    # Search and discovery
    "/search", "/find", "/query", "/discover", "/explore", "/browse",
    
    # User and account related
    "/user", "/users", "/account", "/accounts", "/profile", "/profiles",
    "/member", "/members", "/customer", "/customers", "/client", "/clients",
    
    # Payment and e-commerce
    "/payment", "/payments", "/checkout", "/cart", "/basket", "/order",
    "/orders", "/invoice", "/invoices", "/billing", "/subscription",
    
    # Administrative functions
    "/manage", "/management", "/console", "/control", "/settings",
    "/preferences", "/options", "/configuration", "/setup", "/install",
    "/installation", "/uninstall", "/update", "/upgrade", "/migrate",
    
    # Security scanning endpoints
    "/.git", "/.svn", "/.hg", "/.DS_Store", "/backup", "/backups",
    "/phpinfo.php", "/test.php", "/admin", "/administrator",
    
    # Additional common extensions
    ".jsp", ".asp", ".aspx", ".do", ".action", ".pl", ".cgi", ".py", ".rb",
    ".go", ".rs", ".java", ".class", ".jar", ".war", ".ear", ".dll", ".exe",
    
    # Document files that might contain sensitive info
    ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".odt",
    ".ods", ".odp", ".rtf", ".csv",
    
    # Image files that might be manipulated
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp",
    
    # Source code files
    ".php", ".html", ".htm", ".js", ".css", ".scss", ".less", ".xml",
    ".json", ".yaml", ".yml", ".md", ".txt", ".rst",
    
    # Build and dependency files
    ".lock", ".sum", ".mod", ".dep", ".make", ".mk",
]

SQL_PAYLOADS = [
    "' OR '1'='1", "1' OR '1'='1", "' OR ''='", "1; DROP TABLE users --",
    "' UNION SELECT NULL, username, password FROM users --"
]

XSS_PAYLOADS = [
    "<script>alert('XSS')</script>", "javascript:alert('XSS')",
    "<img src=x onerror=alert('XSS')>", "\"'><script>alert('XSS')</script>"
]

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
    url TEXT PRIMARY KEY,
    title TEXT,
    content TEXT,
    vulnerabilities TEXT
)
""")
conn.commit()

init(autoreset=True)

GENISLIK = 56

print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")

yazi = pyfiglet.figlet_format("AURATOOL")
for satir in yazi.splitlines():
    if len(satir) > GENISLIK:
        satir = satir[:GENISLIK]
    print(Fore.BLUE + f"┃ {Fore.GREEN + Style.BRIGHT}{satir.center(GENISLIK - 2)} {Fore.BLUE}┃")

print(Fore.BLUE + f"┃{' ' * GENISLIK}┃")

print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")

print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")
print(Fore.BLUE + f"┃{Fore.CYAN + '🔥 YIKIMTOOL İNDEX/ SCAN T00L 🔥'.center(GENISLIK)}{Fore.BLUE}┃")
print(Fore.BLUE + f"┃{Fore.MAGENTA + '🚀 CR: @YIKIMTOOL | DEV: @YIKIM44 🚀'.center(GENISLIK)}{Fore.BLUE}┃")
print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")

print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")


def save_page(url, title, content, vulnerabilities=""):
    cursor.execute(
        "INSERT OR REPLACE INTO pages (url, title, content, vulnerabilities) VALUES (?, ?, ?, ?)",
        (url, title, content, vulnerabilities)
    )
    conn.commit()
    print(colored(f"[DB] {url} veritabanına kaydedildi.", "green"))

async def log_vulnerability(vuln_type, url, details, color="yellow"):
    async with aiofiles.open(VULN_LOG_FILE, "a") as f:
        await f.write(f"[{vuln_type}] {url}: {details}\n")
    print(colored(f"[{vuln_type}] {url}: {details}", color))

async def log_info(message):
    print(colored(f"[INFO] {message}", "white"))
    async with aiofiles.open(VULN_LOG_FILE, "a") as f:
        await f.write(f"[INFO] {message}\n")

_robot_parsers = {}

def get_robot_parser(base_url):
    parsed = urlparse(base_url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    if root in _robot_parsers:
        return _robot_parsers[root]
    rp = RobotFileParser()
    robots_url = urljoin(root, "/robots.txt")
    try:
        rp.set_url(robots_url)
        rp.read()
        print(colored(f"[ROBOTS] {robots_url} başarıyla okundu.", "green"))
    except Exception as e:
        print(colored(f"[ROBOTS] {robots_url} okunamadı: {e}", "red"))
        rp = None
    _robot_parsers[root] = rp
    return rp

def is_allowed_by_robots(url):
    rp = get_robot_parser(url)
    if rp is None:
        print(colored(f"[ROBOTS] {url} için robots.txt bulunamadı, erişim varsayılan olarak izinli.", "yellow"))
        return True
    allowed = rp.can_fetch(USER_AGENT, url)
    if not allowed:
        print(colored(f"[ROBOTS] {url} robots.txt tarafından engelleniyor.", "red"))
    return allowed

async def scan_common_files(base_url):
    found = False
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        for path in COMMON_FILES:
            url = urljoin(base_url, path)
            if not is_allowed_by_robots(url):
                await log_vulnerability("ROBOT_BLOCKED", url, "robots.txt tarafından engellendi", "red")
                continue
            try:
                async with session.get(url, timeout=REQUEST_TIMEOUT) as resp:
                    if resp.status == 200:
                        found = True
                        await log_vulnerability("FILE_FOUND", url, "Erişilebilir dosya/dizin bulundu", "yellow")
                    elif resp.status == 403:
                        await log_vulnerability("FORBIDDEN", url, "Erişim engellendi, olası hassas dosya", "yellow")
                    elif resp.status == 404:
                        await log_info(f"{url} bulunamadı (404).")
                    else:
                        await log_info(f"{url} tarandı, durum kodu: {resp.status}")
            except Exception as e:
                await log_vulnerability("ERROR", url, f"Dosya tarama hatası: {e}", "red")
            await asyncio.sleep(RATE_LIMIT_SECONDS)
        if not found:
            await log_info(f"{base_url} için hiçbir hassas dosya/dizin bulunamadı.")

async def scan_sql_injection(url):
    parsed = urlparse(url)
    if not parsed.query:
        await log_info(f"{url} için SQL enjeksiyon testi yapılamadı: Query parametresi yok.")
        return
    found = False
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        for payload in SQL_PAYLOADS:
            test_url = f"{base_url}?{parsed.query}&test={payload}"
            try:
                async with session.get(test_url, timeout=REQUEST_TIMEOUT) as resp:
                    content = await resp.text()
                    if "sql syntax" in content.lower() or "mysql" in content.lower():
                        found = True
                        await log_vulnerability("SQL_INJECTION", test_url, f"Olası SQL Enjeksiyonu: {payload}", "red")
                    else:
                        await log_info(f"SQLi testi ({payload}) için {test_url}: Zafiyet bulunamadı.")
            except Exception as e:
                await log_vulnerability("ERROR", test_url, f"SQLi testi hatası: {e}", "red")
            await asyncio.sleep(RATE_LIMIT_SECONDS)
        if not found:
            await log_info(f"{url} için SQL enjeksiyon zafiyeti tespit edilmedi.")

async def scan_xss(url):
    parsed = urlparse(url)
    if not parsed.query:
        await log_info(f"{url} için XSS testi yapılamadı: Query parametresi yok.")
        return
    found = False
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        for payload in XSS_PAYLOADS:
            test_url = f"{base_url}?{parsed.query}&test={payload}"
            try:
                async with session.get(test_url, timeout=REQUEST_TIMEOUT) as resp:
                    content = await resp.text()
                    if payload in content:
                        found = True
                        await log_vulnerability("XSS", test_url, f"Olası XSS: {payload}", "red")
                    else:
                        await log_info(f"XSS testi ({payload}) için {test_url}: Zafiyet bulunamadı.")
            except Exception as e:
                await log_vulnerability("ERROR", test_url, f"XSS testi hatası: {e}", "red")
            await asyncio.sleep(RATE_LIMIT_SECONDS)
        if not found:
            await log_info(f"{url} için XSS zafiyeti tespit edilmedi.")

async def scan_security_headers(url):
    found = False
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        try:
            async with session.get(url, timeout=REQUEST_TIMEOUT) as resp:
                headers = resp.headers
                missing = []
                if "Content-Security-Policy" not in headers:
                    missing.append("Content-Security-Policy")
                if "X-Frame-Options" not in headers:
                    missing.append("X-Frame-Options")
                if missing:
                    found = True
                    await log_vulnerability("HEADERS", url, f"Eksik güvenlik başlıkları: {', '.join(missing)}", "yellow")
                else:
                    await log_info(f"{url} için tüm güvenlik başlıkları mevcut.")
        except Exception as e:
            await log_vulnerability("ERROR", url, f"Başlık tarama hatası: {e}", "red")
        if not found:
            await log_info(f"{url} için güvenlik başlığı zafiyeti bulunamadı.")

async def scan_vulnerabilities(url):
    await log_info(f"{url} için zafiyet taraması başlatılıyor...")
    await asyncio.gather(
        scan_sql_injection(url),
        scan_xss(url),
        scan_security_headers(url),
        scan_common_files(url)
    )
    await log_info(f"{url} için zafiyet taraması tamamlandı.")

async def fetch_sitemap_links(start_url):
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        parsed = urlparse(start_url)
        root = f"{parsed.scheme}://{parsed.netloc}"
        sitemap_url = urljoin(root, "/sitemap.xml")
        try:
            async with session.get(sitemap_url, timeout=REQUEST_TIMEOUT) as resp:
                if resp.status != 200:
                    await log_info(f"{sitemap_url} erişilemedi (Durum kodu: {resp.status}).")
                    return []
                content = await resp.text()
                soup = BeautifulSoup(content, "xml")
                urls = [u.text.strip() for u in soup.find_all("loc")]
                await log_info(f"{sitemap_url} tarandı, {len(urls)} URL bulundu.")
                return urls
        except Exception as e:
            await log_vulnerability("ERROR", sitemap_url, f"Sitemap okuma hatası: {e}", "red")
            return []

def normalize_link(base, link):
    try:
        joined = urljoin(base, link)
        clean, _ = urldefrag(joined)
        return clean
    except Exception as e:
        print(colored(f"[ERROR] Link normalizasyon hatası ({link}): {e}", "red"))
        return None

def same_domain(a, b):
    return urlparse(a).netloc == urlparse(b).netloc

async def get_links_from_html(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all("a", href=True)
    links = []
    for a in anchors:
        href = a.get("href")
        if not href:
            continue
        n = normalize_link(base_url, href)
        if n:
            links.append(n)
    await log_info(f"{base_url} için {len(links)} link bulundu.")
    return links

async def extract_text_and_title(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        for script in soup(["script", "style", "noscript"]):
            script.extract()
        text = soup.get_text(separator="\n")
        text = re.sub(r'\n\s*\n+', '\n\n', text)
        text = text.strip()
        await log_info(f"Başlık: {title[:50]}..., İçerik uzunluğu: {len(text)} karakter")
        return title, text
    except Exception as e:
        await log_vulnerability("ERROR", "HTML işleme", f"Metin/başlık çıkarma hatası: {e}", "red")
        return "", ""

async def scrape_and_save(url):
    if not is_allowed_by_robots(url):
        await log_vulnerability("ROBOT", url, "robots.txt izin vermiyor", "red")
        return False, ""
    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        try:
            async with session.get(url, timeout=REQUEST_TIMEOUT) as resp:
                if resp.status != 200:
                    await log_vulnerability("HTTP", url, f"Durum kodu: {resp.status}", "yellow")
                    return False, ""
                content = await resp.text()
                title, text = await extract_text_and_title(content)
                await scan_vulnerabilities(url)
                save_page(url, title, text, "Scanned")
                print(colored(f"[OK] Kaydedildi: {url} ({len(text)} chars)", "green"))
                return True, content
        except Exception as e:
            await log_vulnerability("ERROR", url, f"Scrape hatası: {e}", "red")
            return False, ""

async def crawl(start_url, max_depth=1, max_pages=MAX_PAGES_DEFAULT, scan_all_web=False):
    start_url = normalize_link(start_url, start_url)
    if start_url is None:
        print(colored("Geçersiz başlangıç URL'si.", "red"))
        return
    domain = urlparse(start_url).netloc
    to_visit = [(start_url, 0)]
    visited = set()
    pages_visited = 0

    sitemap_links = await fetch_sitemap_links(start_url)
    if sitemap_links:
        print(colored(f"[SITEMAP] {len(sitemap_links)} URL bulundu; listeye ekleniyor.", "green"))
        for u in sitemap_links:
            n = normalize_link(start_url, u)
            if n and (scan_all_web or same_domain(start_url, n)):
                to_visit.append((n, 0))

    async with aiohttp.ClientSession(headers={"User-Agent": USER_AGENT}) as session:
        while to_visit and pages_visited < max_pages:
            url, depth = to_visit.pop(0)
            if url in visited:
                await log_info(f"{url} zaten ziyaret edildi, atlanıyor.")
                continue
            if depth > max_depth:
                await log_info(f"{url} maksimum derinlik ({max_depth}) aşıldı, atlanıyor.")
                continue
            if not scan_all_web and not same_domain(start_url, url):
                await log_info(f"{url} farklı domainde, atlanıyor.")
                continue
            visited.add(url)

            print(colored(f"[CRAWL] Derinlik={depth} -> {url}", "white"))
            success, content = await scrape_and_save(url)
            if not success:
                continue
            pages_visited += 1

            links = await get_links_from_html(url, content)
            for l in links:
                if l not in visited and (scan_all_web or same_domain(start_url, l)):
                    to_visit.append((l, depth + 1))
            await asyncio.sleep(RATE_LIMIT_SECONDS)

    print(colored(f"[FINISH] Toplam ziyaret edilen sayfa: {pages_visited}", "green"))

def create_or_update_index():
    schema = Schema(url=ID(stored=True), title=TEXT(stored=True), content=TEXT, vulnerabilities=TEXT)
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        print(colored(f"[INDEX] {INDEX_DIR} dizini oluşturuldu.", "green"))
    if not exists_in(INDEX_DIR):
        ix = create_in(INDEX_DIR, schema)
        print(colored(f"[INDEX] Yeni index oluşturuldu.", "green"))
    else:
        ix = open_dir(INDEX_DIR)
        print(colored(f"[INDEX] Mevcut index açıldı.", "green"))

    writer = ix.writer()
    for row in cursor.execute("SELECT url, title, content, vulnerabilities FROM pages"):
        url, title, content, vulnerabilities = row
        try:
            writer.update_document(url=url, title=title or "", content=content or "", vulnerabilities=vulnerabilities or "")
            print(colored(f"[INDEX] {url} indekslendi.", "white"))
        except Exception as e:
            print(colored(f"[INDEX ERR] {url} -> {e}", "red"))
    writer.commit()
    print(colored("[INDEX] İşlem tamamlandı.", "green"))

def search_index(query_str, limit=20):
    if not exists_in(INDEX_DIR):
        print(colored("Index yok. Önce 'index' komutunu çalıştır.", "red"))
        return
    ix = open_dir(INDEX_DIR)
    qp = QueryParser("content", ix.schema)
    q = qp.parse(query_str)
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=limit)
        if not results:
            print(colored("Sonuç yok.", "yellow"))
            return
        for i, r in enumerate(results):
            print(colored(f"{i+1}. {r['url']} | {r.get('title','')[:80]} | Vulns: {r.get('vulnerabilities','')}", "white"))

def print_help():
    help_text = """
Kullanım komutları:
  crawl <start_url> [max_depth] [max_pages] [all_web]  - Taramayı başlatır (aynı domain veya tüm web)
  index                                               - Veritabanındaki sayfaları Whoosh indexine basar
  search <sorgu> - İndeks üzerinde arama yapar
  scan <url> - Belirtilen URL'de zafiyet taraması yapar
  show <url> - Veritabanındaki bir sayfayı gösterir
  help - yardım
  exit  - Çıkış
"""
    print(colored(help_text, "white"))

def show_saved_page(url):
    cursor.execute("SELECT url, title, content, vulnerabilities FROM pages WHERE url = ?", (url,))
    row = cursor.fetchone()
    if not row:
        print(colored("Kayıt bulunamadı.", "red"))
        return
    print(colored(f"URL: {row[0]}", "white"))
    print(colored(f"Title: {row[1]}", "white"))
    print(colored(f"Vulnerabilities: {row[3]}", "yellow"))
    print(colored("--- Content (ilk 1000 chars) ---", "white"))
    print(colored(row[2][:1000], "white"))

async def cli_loop():
    print(colored("=== aura-team Index ve Zafiyet Tarama Aracı CLI ===", "green"))
    print_help()
    while True:
        try:
            raw = input(colored(">> ", "white")).strip()
        except (KeyboardInterrupt, EOFError):
            print(colored("\nÇıkılıyor...", "red"))
            break
        if not raw:
            continue
        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd == "help":
            print_help()
        elif cmd == "exit":
            print(colored("Çıkış yapılıyor.", "red"))
            break
        elif cmd == "crawl":
            if not args:
                print(colored("Usage: crawl <start_url> [max_depth] [max_pages] [all_web]", "red"))
                continue
            start = args[0]
            max_depth = int(args[1]) if len(args) >= 2 else 1
            max_pages = int(args[2]) if len(args) >= 3 else MAX_PAGES_DEFAULT
            scan_all_web = args[3].lower() == "true" if len(args) >= 4 else False
            await crawl(start, max_depth=max_depth, max_pages=max_pages, scan_all_web=scan_all_web)
        elif cmd == "index":
            create_or_update_index()
        elif cmd == "search":
            if not args:
                print(colored("Usage: search <query>", "red"))
                continue
            q = " ".join(args)
            search_index(q)
        elif cmd == "scan":
            if not args:
                print(colored("Usage: scan <url>", "red"))
                continue
            await scan_vulnerabilities(args[0])
        elif cmd == "show":
            if not args:
                print(colored("Usage: show <url>", "red"))
                continue
            show_saved_page(args[0])
        else:
            print(colored("Bilinmeyen komut. 'help' yaz.", "red"))

if __name__ == "__main__":
    asyncio.run(cli_loop())