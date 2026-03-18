import requests,json,random,string,uuid,re,pyfiglet,threading,itertools,time,sys
from colorama import Fore,Style,init
init(autoreset=True)
B=Style.BRIGHT
logo=pyfiglet.figlet_format("TikTok")
print(Fore.MAGENTA+B+logo+Fore.YELLOW+B+"@Zeynalovs5")
use=input(Fore.CYAN+B+"👉 TikTok Kullanıcı Adını Gir: "+Style.RESET_ALL)
adet=int(input(Fore.GREEN+B+"👉 Kaç Takipçi Gönderilsin? "+Style.RESET_ALL))
def get_token():
    url="https://www.ttboost.app/api/login"
    device_name=''.join(random.choices(string.digits,k=8))+''.join(random.choices(string.ascii_uppercase,k=2))
    android_id=uuid.uuid4().hex[:16]
    username=''.join(random.choices(string.ascii_lowercase,k=5))
    payload={"device_name":device_name,"id":android_id,"referral":None,"username":username}
    headers={'User-Agent':"ktor-client",'Accept':"application/json",'Accept-Encoding':"gzip",'Content-Type':"application/json",'hash':"f3306e1b14321996320eaca84b2250fa7a8506f92e29274e67125b1f81b45726",'accept-charset':"UTF-8"}
    r=requests.post(url,data=json.dumps(payload),headers=headers)
    return r.json()['data']['token']
def get_profile_image(username):
    url=f"https://www.tiktok.com/@{username}"
    headers={'User-Agent':"Mozilla/5.0",'Connection':"Keep-Alive",'Accept-Encoding':"gzip"}
    r=requests.get(url,headers=headers)
    m=re.search(r'https:\\u002F\\u002F[^\s"]+:100:100\.jpeg[^\s"]*',r.text)
    if m:return m.group(0).replace("\\u002F","/")
    else:
        print(Fore.RED+B+"❌ Profil resmi alınamadı!")
        exit()
def loading_animation(stop_event):
    for c in itertools.cycle(['|','/','-','\\']):
        if stop_event.is_set():break
        sys.stdout.write(Fore.YELLOW+B+'\r⚙️ Takipçiler gönderiliyor... '+c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r'+' '*50+'\r')
def send_follower(username,image,index,total):
    try:
        token=get_token()
        url="https://www.ttboost.app/api/orders"
        payload={"image":image,"url":f"https://www.tiktok.com/@{username}/","username":username,"product_id":27,"purchase_token":None}
        headers={'User-Agent':"ktor-client",'Accept':"application/json",'Accept-Encoding':"gzip",'Content-Type':"application/json",'authorization':f"Bearer {token}",'accept-charset':"UTF-8"}
        r=requests.post(url,data=json.dumps(payload),headers=headers)
        res=r.json()
        if res.get("success"):print(Fore.CYAN+B+f"\n✅ [{index}/{total}] {username} kullanıcısına takipçi gönderildi")
        else:print(Fore.RED+B+f"\n❌ [{index}/{total}] Hata: {res.get('error_code')}")
    except Exception as e:print(Fore.RED+B+f"\n⚠️ [{index}/{total}] İstek hatası: {e}")
def main():
    image=get_profile_image(use)
    stop_event=threading.Event()
    t=threading.Thread(target=loading_animation,args=(stop_event,))
    t.start()
    threads=[]
    for i in range(1,adet+1):
        th=threading.Thread(target=send_follower,args=(use,image,i,adet))
        threads.append(th)
        th.start()
        time.sleep(0.2)
    for th in threads:th.join()
    stop_event.set()
    t.join()
    print(Fore.GREEN+B+"\n🎉 Tüm takipçi gönderme işlemleri tamamlandı!")
main()
