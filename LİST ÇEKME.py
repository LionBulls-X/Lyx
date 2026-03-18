import random  
import string  
import json  
import requests  
from concurrent.futures import ThreadPoolExecutor  
import os  
import pyfiglet  
from colorama import Fore, Style, init  
from time import sleep, time  
import threading  
import signal  
from Topython import Instagram  
  
G = Fore.LIGHTGREEN_EX  
Y = Fore.LIGHTYELLOW_EX  
R = Fore.LIGHTRED_EX  
S = Style.RESET_ALL  
  
init(autoreset=True)  
  
GENISLIK = 56  
  
print(Fore.LIGHTBLUE_EX + "┃" + "━" * GENISLIK + "┃")  
yazi = pyfiglet.figlet_format("YIKIM T00L")  
for satir in yazi.splitlines():  
    if len(satir) > GENISLIK:  
        satir = satir[:GENISLIK]  
    print(Fore.BLUE + f"┃ {Fore.GREEN + Style.BRIGHT}{satir.center(GENISLIK - 2)} {Fore.BLUE}┃")  
print(Fore.BLUE + f"┃{' ' * GENISLIK}┃")  
print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")  
print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")  
print(Fore.BLUE + f"┃{Fore.CYAN + '🔥 YIKIM LIST ÇEKME [2026] 🔥'.center(GENISLIK)}{Fore.BLUE}┃")  
print(Fore.BLUE + f"┃{Fore.MAGENTA + '🚀 CR: @YIKIMTOOL | DEV: @YIKIM44 🚀'.center(GENISLIK)}{Fore.BLUE}┃")  
print(Fore.BLUE + f"┃{'*' * GENISLIK}┃")  
print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")  
print("\n")  
print(Fore.BLUE + "┃" + "━" * GENISLIK + "┃")  
print(f"""   
{R} LIST ÇEKİM YIL ID ARALIGI LİSTESİ {S}  

{G} - 2010 AKTIF ✅ {S}  
{G} - 2011 AKTIF ✅ {S}  
{G} - 2012 AKTIF ✅ {S}  
{G} - 2013 AKTIF ✅ {S}  
{G} - 2014 AKTIF ✅ {S}  
{G} - 2015 AKTIF ✅ {S}  
{G} - 2016 AKTIF ✅ {S}  
{G} - 2017 AKTIF ✅ {S}  
{G} - 2018 AKTIF ✅ {S}  
{G} - 2019 AKTIF ✅ {S}  
{G} - 2020 AKTIF ✅ {S}  
{G} - 2021 AKTIF ✅ {S}  
{G} - 2022 AKTIF ✅ {S}  
{G} - 2023 AKTIF ✅ {S}  
{G} - 2024 AKTIF ✅ {S}  
{G} - 2025 AKTIF ✅ {S}  
  
       {Y} THİS T00L CHANNEL: https://t.me/YIKIMTOOL {S}  
""")  
print(Fore.LIGHTBLUE_EX + "┃" + "━" * GENISLIK + "┃")  
D = input(" save dosya ismi gir (uzantısız!):")  
  
  
print_lock = threading.Lock()  
stop_event = threading.Event()  
  
def hand(sig, frame):  
    stop_event.set()  
  
signal.signal(signal.SIGINT, hand)  
  
def ipv4():  
    return ".".join(str(random.randint(1, 254)) for _ in range(4))  
  
def hadrs():  
    fake_ip = ipv4()  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 12.0.0.16.90',  
        'Accept': '*/*',  
        'Accept-Language': 'en-US,en;q=0.9',  
        'Accept-Encoding': 'gzip, deflate, br',  
        'Connection': 'keep-alive',  
        'X-Forwarded-For': fake_ip,  
        'X-Client-IP': fake_ip,  
        'X-Originating-IP': fake_ip,  
        'X-Remote-Addr': fake_ip,  
        'X-Forwarded-Host': fake_ip,  
    }  
    return headers  
  
def is_valid_username(username):  
    return username and 3 <= len(username) <= 30 and username[0].isalpha() and all(c.isalnum() or c in ['_'] for c in username)  
  
def fetch_user(user_id, file_path, lock, ranges):  
    try:  
        start, end, _ = random.choice(ranges)  
        user_id = random.randint(start, end)  
        url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"  
        headers = hadrs()  
          
        response = requests.get(url, headers=headers, timeout=5)  
          
        if response.status_code == 200:  
            try:  
                json_data = response.json()  
                if 'user' in json_data and json_data['user']:  
                    username = json_data['user'].get('username')  
                    if username and is_valid_username(username):  
                        with lock:  
                            with open(file_path, "a", encoding='utf-8') as fr:  
                                fr.write(username + "\n")  
                        return 1, f"\x1b[1;32m + {username} bulundu\x1b[0m"  
                return 0, None  
            except json.JSONDecodeError:  
                return 0, None  
        elif response.status_code == 429:  
            return 0, f"\x1b[1;33m Rate limit hit, slowing down\x1b[0m"  
        elif response.status_code == 401:  
            return 0, None  
        elif response.status_code in [403, 404, 400]:  
            return 0, None  
        else:  
            return 0, f"\x1b[1;31m Unexpected status: {response.status_code}\x1b[0m"  
    except requests.exceptions.RequestException:  
        return 0, None  
    except Exception as e:  
        return 0, None  
  
def fetch_list(file_path, ranges, num_requests=10000, max_workers=10):  
    found_count = 0  
    attempt_count = 0  
    lock = threading.Lock()  
    consecutive_429 = 0  
      
    with ThreadPoolExecutor(max_workers=max_workers) as executor:  
        futures = []  
        for _ in range(num_requests):  
            if stop_event.is_set():  
                break  
            user_id = 0  
            futures.append(executor.submit(fetch_user, user_id, file_path, lock, ranges))  
              
            if len(futures) >= max_workers * 2:  
                for future in futures:  
                    if stop_event.is_set():  
                        break  
                    count, msg = future.result()  
                    attempt_count += 1  
                    found_count += count  
                    if msg:  
                        with print_lock:  
                            print(msg)  
                      
                    if "Rate limit" in msg if msg else False:  
                        consecutive_429 += 1  
                        delay = min(10 * consecutive_429, 60)  
                        sleep(delay)  
                        consecutive_429 = max(0, consecutive_429 - 1)  
                      
                    if attempt_count % 100 == 0:  
                        with print_lock:  
                            print(f"\x1b[1;36m Processed {attempt_count} attempts, found {found_count} so far\x1b[0m")  
                  
                futures = []  
          
        for future in futures:  
            if stop_event.is_set():  
                break  
            count, msg = future.result()  
            attempt_count += 1  
            found_count += count  
            if msg:  
                with print_lock:  
                    print(msg)  
              
            if "Rate limit" in msg if msg else False:  
                consecutive_429 += 1  
                delay = min(10 * consecutive_429, 60)  
                sleep(delay)  
                consecutive_429 = max(0, consecutive_429 - 1)  
              
            if attempt_count % 100 == 0:  
                with print_lock:  
                    print(f"\x1b[1;36m Processed {attempt_count} attempts, found {found_count} so far\x1b[0m")  
      
    with print_lock:  
        print(f"\x1b[1;36m Task completed: {attempt_count} attempts, {found_count} found\x1b[0m")  
    return found_count  
  
yillar = [2010, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]  
  
def yıkım2():  
    with open(f'{D}.txt', 'a', encoding='utf-8') as dosya:  
        failures = 0  
        while not stop_event.is_set():  
            cycle_finds = 0  
            for yil in yillar:  
                if stop_event.is_set():  
                    break  
                try:  
                    kullanici_adi = Instagram.GenUsers(date=yil)  
                    if kullanici_adi:  
                        dosya.write(kullanici_adi + '\n')  
                        dosya.flush()  
                        with print_lock:  
                            print(f"\033[1;36m{kullanici_adi}\033[0m")  
                        cycle_finds += 1  
                except Exception as e:  
                    with print_lock:  
                        print(f"\033[1;31mHata ({yil}): {e}\033[0m")  
            if cycle_finds < 20:  
                failures += 1  
            else:  
                failures = 0  
            if failures >= 3:  
                with print_lock:  
                    print(f"\033[1;31m thread stopping after 3 low cycles\033[0m")  
                break  
  
def yıkım3():  
    threadler = [threading.Thread(target=yıkım2, daemon=True) for _ in range(700)]  
    for thread in threadler:  
        thread.start()  
  
def yikim():  
    ranges = [  
        (1, 1279000, 2010),  
        (1279001, 17750000, 2011),  
        (17750001, 279760000, 2012),  
        (279760001, 900990000, 2013),  
        (900990001, 1629010000, 2014),  
        (1629010001, 1900000000, 2015),  
        (1900000001, 2500000000, 2016),  
        (2500000001, 3713668786, 2017),  
        (3713668787, 5699785217, 2018),  
        (5699785218, 8507940634, 2019),  
        (8507940635, 10500000000, 2020)  
    ]  
      
    with print_lock:  
        print("\x1b[1;39m—" * 60)  
          
        print("\x1b[1;39m—" * 60)  
        print("\x1b[1;36m[cyan]Tüm yıllardan karışık çekim başlatılıyor.. \x1b[0m")  
      
    file_path = f"{D}.txt"  
    if os.path.exists(file_path):  
        with open(file_path, 'r', encoding='utf-8') as f:  
            mevcut = len([line for line in f if line.strip()])  
        with print_lock:  
            print(f"\x1b[1;34m[blue]Mevcut kullanıcılar: {mevcut}\x1b[0m")  
    else:  
        mevcut = 0  
      
    toplam_bulunan = 0  
    while not stop_event.is_set():  
        batch_finds = []  
        for attempt in range(3):  
            if stop_event.is_set():  
                break  
            year_found = fetch_list(file_path, ranges, num_requests=7000, max_workers=70)  
            batch_finds.append(year_found)  
            with print_lock:  
                print(f"\x1b[1;36m attempt {attempt+1}: {year_found} found\x1b[0m")  
        if all(f < 20 for f in batch_finds):  
            with print_lock:  
                print(f"\x1b[1;31m failed 3 attempts with <20 each, stopping KOD1\033[0m")  
            break  
        total_batch = sum(batch_finds)  
        toplam_bulunan += total_batch  
        with print_lock:  
            print(f"\x1b[1;32m[bold green]Karışık çekim batch tamamlandı: {total_batch} yeni kullanıcı bulundu. Toplam: {mevcut + toplam_bulunan}\x1b[0m")  
        sleep(1)  
  
if __name__ == "__main__":  
    yıkım3()  
    kod1_thread = threading.Thread(target=yikim)  
    kod1_thread.start()  
    kod1_thread.join()
