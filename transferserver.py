import requests, json, time, colorama, datetime
from colorama import Fore

colorama.init()
with open('config.json') as f:
    data = json.load(f)

serverid = int(input("Enter Guild ID: "))
ownerid = input("Enter Owner ID: ")
token = data["TOKEN"]
timer = data["SLEEP"]
proxyf = data["PROXY"]
proxyr = data["customPROXY"]
proxyurl = data["customPROXY-URL"]

headers = {
	"authorization": token,
	"content-type": "application/json",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1011 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36"
}

paylod = {
	"owner_id": ownerid
}

proxies = dict(https='socks5://185.176.58.20:1080')
proxiesr = dict(https=f'socks5://{proxyurl}')

time.sleep(timer)
start_time = time.time()
if proxyf == True:
    if proxyr == True:
        x = requests.patch(f'https://canary.discord.com/api/v9/guilds/{serverid}', json=paylod, headers=headers, proxies=proxiesr)
    elif proxyr == False:
        x = requests.patch(f'https://canary.discord.com/api/v9/guilds/{serverid}', json=paylod, headers=headers, proxies=proxies)
elif proxyf == False:
    x = requests.patch(f'https://canary.discord.com/api/v9/guilds/{serverid}', json=paylod, headers=headers)

elapsed = '%.3fs' % (time.time() - start_time)
if x.status_code == 200:
    print(f"[!] {Fore.RED}Guild successfully transferred. | " + elapsed + Fore.RESET)
    time.sleep(10)
