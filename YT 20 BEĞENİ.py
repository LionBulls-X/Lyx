import requests, time
hacu = input ("• VİDEO LİNKİ GİR KNK: ")
cookies = {
    'PHPSESSID': '4d1e2b4dd4001639c531f5166d32e541',
    '_gcl_au': '1.1.257501761.1748777870',
    '_ga': 'GA1.1.1550297975.1748777870',
    'colorMode': 'sun',
    'cfz_zaraz-analytics': '%7B%22_cfa_clientId%22%3A%7B%22v%22%3A%2242511059969347770%22%2C%22e%22%3A1780313871578%7D%2C%22_cfa_sId%22%3A%7B%22v%22%3A%2214635443432284490%22%2C%22e%22%3A1748779675709%7D%7D',
    '_ga_MLEM1KHQDX': 'GS2.1.s1748777869$o1$g1$t1748777945$j60$l0$h1940825991$dT_tEV8XnfrX6HTJ5FRjlAkFTXSQzDrYPdg',
}

headers = {
    'authority': 'roxmedya.com.tr',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=4d1e2b4dd4001639c531f5166d32e541; _gcl_au=1.1.257501761.1748777870; _ga=GA1.1.1550297975.1748777870; colorMode=sun; cfz_zaraz-analytics=%7B%22_cfa_clientId%22%3A%7B%22v%22%3A%2242511059969347770%22%2C%22e%22%3A1780313871578%7D%2C%22_cfa_sId%22%3A%7B%22v%22%3A%2214635443432284490%22%2C%22e%22%3A1748779675709%7D%7D; _ga_MLEM1KHQDX=GS2.1.s1748777869$o1$g1$t1748777945$j60$l0$h1940825991$dT_tEV8XnfrX6HTJ5FRjlAkFTXSQzDrYPdg',
    'origin': 'https://roxmedya.com.tr',
    'referer': 'https://roxmedya.com.tr/youtube-ucretsiz-begeni/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'ns_action': 'freetool_start',
    'freetool[id]': '30',
    'freetool[token]': '',
    'freetool[process_item]': hacu,
    'freetool[quantity]': '20',
}

try:
	response = requests.post('https://roxmedya.com.tr/action/', cookies=cookies, headers=headers, data=data)
	batu = response.json()
	bekleamk = batu.get ('freetool_delay_minute')
	t = batu.get('freetool_process_token')
	print ("• TOKEN: " + t)
	print ("_-" *30)
	print ("• SÜRE: " + bekleamk + " Dakika")
	print ("_-" *30)
	print (bekleamk + " Dakika Bekleniyor...")
	time.sleep(int(bekleamk) * 60)
	print ("_-" *30)
except:
	print (response.text)
	
cookies = {
    'PHPSESSID': '4d1e2b4dd4001639c531f5166d32e541',
    '_gcl_au': '1.1.257501761.1748777870',
    '_ga': 'GA1.1.1550297975.1748777870',
    'colorMode': 'sun',
    'cfz_zaraz-analytics': '%7B%22_cfa_clientId%22%3A%7B%22v%22%3A%2242511059969347770%22%2C%22e%22%3A1780313871578%7D%2C%22_cfa_sId%22%3A%7B%22v%22%3A%2214635443432284490%22%2C%22e%22%3A1748779675709%7D%7D',
    '_ga_MLEM1KHQDX': 'GS2.1.s1748777869$o1$g1$t1748777945$j60$l0$h1940825991$dT_tEV8XnfrX6HTJ5FRjlAkFTXSQzDrYPdg',
}

headers = {
    'authority': 'roxmedya.com.tr',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=4d1e2b4dd4001639c531f5166d32e541; _gcl_au=1.1.257501761.1748777870; _ga=GA1.1.1550297975.1748777870; colorMode=sun; cfz_zaraz-analytics=%7B%22_cfa_clientId%22%3A%7B%22v%22%3A%2242511059969347770%22%2C%22e%22%3A1780313871578%7D%2C%22_cfa_sId%22%3A%7B%22v%22%3A%2214635443432284490%22%2C%22e%22%3A1748779675709%7D%7D; _ga_MLEM1KHQDX=GS2.1.s1748777869$o1$g1$t1748777945$j60$l0$h1940825991$dT_tEV8XnfrX6HTJ5FRjlAkFTXSQzDrYPdg',
    'origin': 'https://roxmedya.com.tr',
    'referer': 'https://roxmedya.com.tr/youtube-ucretsiz-begeni/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'ns_action': 'freetool_start',
    'freetool[id]': '30',
    'freetool[token]': t,
    'freetool[process_item]': hacu,
    'freetool[quantity]': '20',
}

response = requests.post('https://roxmedya.com.tr/action/', cookies=cookies, headers=headers, data=data)
print (response.text)	
