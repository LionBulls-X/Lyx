import os, random, requests
try: 
    from user_agent import generate_user_agent
except ModuleNotFoundError: 
    os.system('pip install user_agent && clear && exit()')

r = requests.post(
    'https://api.likesjet.com/freeboost/3', 
    json={
        'link': input('Video Linki Girin : '), 
        'tiktok_username': input('TikTok Kullanıci adi : '), 
        'email': f'THOMASHACK{random.randint(10000, 99999)}@gmail.com'
    }, 
    headers={ 
        'Host': 'api.likesjet.com', 
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
        'accept-language': 'en-US,en;q=0.9', 
        'cache-control': 'max-age=0', 
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"', 
        'sec-ch-ua-mobile': '?1', 
        'sec-ch-ua-platform': '"Android"', 
        'sec-fetch-dest': 'document', 
        'sec-fetch-mode': 'navigate', 
        'sec-fetch-site': 'none', 
        'sec-fetch-user': '?1', 
        'upgrade-insecure-requests': '1', 
        'user-agent': generate_user_agent()
    }
).json()

print('Başarıyla 1000 görüntüleme gönderildi. İyi seyirler!' if r.get('status') else "Sorry, couldn't send views to your video.")