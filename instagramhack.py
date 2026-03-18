import time
import os
import random

def banner():
    os.system('clear')
    print("""
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗      █████╗ ██████╗     ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║     ██╔══██╗██╔══██╗    ██║
███████║███████║██║     █████╔╝ ██║     ███████║██████╔╝    ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██║     ██╔══██║██╔═══╝     ██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██║         ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═╝
                BruteForce by HackLab-lyonX
    """)

def simulate_attack(username, wordlist):
    print(f"\n[+] Target: {username}")
    print(f"[+] Wordlist: {wordlist if wordlist else 'Generated automatically'}")
    print("[+] Simulating attack...\n")
    
    start_time = time.time()
    while time.time() - start_time < 300:  # 5 dəqiqə (300 saniyə)
        fake_pass = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        print(f"[*] Trying password: {fake_pass}")
        time.sleep(1.5)  # hər sınaq üçün gecikmə
    
    print("\n[✔] This was just a test simulation. No real hacking occurred.")
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠿⠛⠉⠉⢀⣀⣀⡀⠉⠉⠛⠻⢿⣷⣦⣄⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⠋⠀⠀⠀⠀⠀⣾⣿⠿⠛⠃⠀⠀⠀⠀⠀⠙⣿⣿⣧⠀⠀
⠀⠀⠀⣠⣾⣿⠃⠀⠀⠀⠀⠀⠈⢻⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠈⣿⣿⣷⡀
⠀⠀⣼⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣷⣦⣤⣤⣤⣤⣶⣿⣿⣿⡇
⠀⠀⣿⣿⣿⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⢿⣿⣿⠿⠋⠀⠀
⠀⠀⠀⠉⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

# Başlanğıc
banner()
target = input("[?] Enter Instagram username: ")
use_custom_wordlist = input("[?] Do you have a wordlist file? (y/n): ").lower()

if use_custom_wordlist == 'y':
    wordlist_path = input("[?] Enter wordlist path: ")
else:
    wordlist_path = None
    print("[*] Generating default wordlist... (simulated)")

simulate_attack(target, wordlist_path)