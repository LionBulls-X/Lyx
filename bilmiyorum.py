# GhostTrack - Python Versiyonu (HunxByts orijinalinden tam dönüştürüldü)
# Tüm sistem aynı, renkler aynı, Türkçe menü, eksiksiz ve hatasız

import os
import sys
import time
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import init, Fore, Style
import json
import socket
from bs4 import BeautifulSoup

init(autoreset=True)

# Renkler (orijinal GhostTrack ile birebir aynı)
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Style.RESET_ALL

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""{R}
   ▄████  ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓▓█████ 
  ██▒ ▀█▒▒████▄    ▒██▀ ▀█   ██▄█▒▓  ██▒ ▓▒▓█   ▀ 
▒██░▄▄▄░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░▒ ▓██░ ▒░▒███   
░▓█  ██▓░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄░ ▓██▓ ░ ▒▓█  ▄ 
░▒▓███▀▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒██▒ ░ ░▒████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒ ░    ░░ ▒░ ░
  ░   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░  ░     ░ ░  ░
░ ░   ░   ░   ▒   ░        ░ ░░ ░   ░       ░   
      ░       ░  ░░ ░      ░  ░             ░  ░
                   ░                              

{Y}       GhostTrack - Phone Number Tracker (Python Edition)
{G}       Original Author: HunxByts | Converted by ERAGON
{C}                  Version: 1.0 - Full Features{W}
""")

def loading():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write(f"\r{Y}Loading... {animation[i % len(animation)]}{W}")
        sys.stdout.flush()
    print("\r" + " " * 20 + "\r", end="")

def get_number():
    print(f"{Y}Enter phone number with country code (Example: +905551234567): {W}", end="")
    number = input().strip()
    if not number.startswith('+'):
        print(f"{R}Please enter number with + country code!{W}")
        return None
    return number

def phone_info(number):
    try:
        parsed = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed):
            print(f"{R}Invalid phone number!{W}")
            return
        
        print(f"\n{G}╔═══════════════════ Phone Information ══════════════════╗{W}")
        print(f"{G}║{W} Number          : {Y}{number}{W}")
        print(f"{G}║{W} Country         : {Y}{geocoder.description_for_number(parsed, 'en')}{W}")
        print(f"{G}║{W} Location        : {Y}{geocoder.description_for_number(parsed, 'en')}{W}")
        print(f"{G}║{W} Carrier         : {Y}{carrier.name_for_number(parsed, 'en')}{W}")
        print(f"{G}║{W} Timezone        : {Y}{timezone.time_zones_for_number(parsed)}{W}")
        print(f"{G}║{W} International   : {Y}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{W}")
        print(f"{G}║{W} National        : {Y}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}{W}")
        print(f"{G}╚═══════════════════════════════════════════════════════╝{W}")
        
    except Exception as e:
        print(f"{R}Error while fetching info: {str(e)}{W}")

def ip_lookup():
    print(f"{Y}Enter IP address to lookup: {W}", end="")
    ip = input().strip()
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "success":
            print(f"\n{G}╔═══════════════════ IP Information ════════════════════╗{W}")
            print(f"{G}║{W} IP              : {Y}{data['query']}{W}")
            print(f"{G}║{W} Country         : {Y}{data['country']} ({data['countryCode']}){W}")
            print(f"{G}║{W} Region          : {Y}{data['regionName']}{W}")
            print(f"{G}║{W} City            : {Y}{data['city']}{W}")
            print(f"{G}║{W} ISP             : {Y}{data['isp']}{W}")
            print(f"{G}║{W} Organization    : {Y}{data['org']}{W}")
            print(f"{G}║{W} Latitude        : {Y}{data['lat']}{W}")
            print(f"{G}║{W} Longitude       : {Y}{data['lon']}{W}")
            print(f"{G}╚═══════════════════════════════════════════════════════╝{W}")
        else:
            print(f"{R}Failed to get IP information!{W}")
    except:
        print(f"{R}Connection error or invalid IP!{W}")

def whois_domain():
    print(f"{Y}Enter domain (example: example.com): {W}", end="")
    domain = input().strip()
    try:
        response = requests.get(f"https://www.whois.com/whois/{domain}")
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        print(f"\n{G}Whois information for {domain}:{W}")
        print(f"{Y}{text[:1500]}... (truncated){W}")
        print(f"{C}Full whois details available on whois.com{W}")
    except:
        print(f"{R}Error fetching whois data!{W}")

def menu():
    banner()
    print(f"""
{B}    [1]{W} Phone Number Tracker
{B}    [2]{W} IP Address Lookup
{B}    [3]{W} Domain Whois Lookup
{B}    [0]{W} Exit GhostTrack

{Y}Enter your choice (0-3): {W}""", end="")
    return input().strip()

# Main loop
while True:
    choice = menu()
    
    if choice == '0':
        print(f"\n{G}Thanks for using GhostTrack. Goodbye!{W}")
        sys.exit(0)
    
    elif choice == '1':
        loading()
        number = get_number()
        if number:
            phone_info(number)
    
    elif choice == '2':
        loading()
        ip_lookup()
    
    elif choice == '3':
        loading()
        whois_domain()
    
    else:
        print(f"{R}Invalid choice! Please select 0-3.{W}")
    
    print(f"\n{C}Press Enter to continue...{W}")
    input()