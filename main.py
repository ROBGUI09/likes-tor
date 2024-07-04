import requests, random
from fake_useragent import UserAgent
ua = UserAgent()

url = "https://xn--80aaahf3a6anlhog.xn--p1ai/inap/likes"
payload = {"path":"participants","id":"49477"}

count = 4000

def gen_session():
    session = requests.session()
    creds = str(random.randint(10000,0x7fffffff)) + ":" + "foobar"
    session.proxies = {'http': 'socks5h://{}@localhost:9050'.format(creds), 'https': 'socks5h://{}@localhost:9050'.format(creds)}
    return session

for i in range(count):
    print(i,'/',count)
    session = gen_session()
    r = session.post(url,headers={"User-Agent":ua.random},json=payload).json()
    print(r["message"])
    res = r["status"] == "success"
    while res != True:
        print("лох")
        try:
            session = gen_session()
            r = session.post(url,headers={"User-Agent":ua.random},json=payload).json()
            print(r["message"])
            res = r["status"] == "success"
        except Exception as e:
            print(type(e),"hope that explains much")

