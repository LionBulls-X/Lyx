import requests
import json
import ast
user = input("Enter Any User TikTok Name : ")
res = requests.post("https://ttpub.linuxtech.io:5004/api/search", data=json.dumps({"username": user}), headers = {'Host': "ttpub.linuxtech.io:5004",'User-Agent': "Dart/3.5 (dart:io)",'Accept-Encoding': "gzip",'Content-Type': "application/json"})
ses = res.json()['user']["sid"]
response = requests.post("https://ttpub.linuxtech.io:5004/api/search_by_sid_build_request", data=json.dumps({"sid": ses,"count_requests": 3}), headers = {'Host': "ttpub.linuxtech.io:5004",'User-Agent': "Dart/3.5 (dart:io)",'Accept-Encoding': "gzip",'Content-Type': "application/json"}).json()
url2 = response['request'][0]["url"]
head = ast.literal_eval(response['request'][0]["headers"])
req = requests.get(url2, headers=head).text
print(req)
#@darkv3rtex