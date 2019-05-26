# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, unquote


post_data = {
    '_csrf': 'kdfjal', 
    'LoginForm[username]': '17605888676',
    'LoginForm[password]': 'ybb2601169057',
    'LoginForm[rememberMe]': '0'
}

response = requests.get(url='https://passport.21cnjy.com/login')
soup = BeautifulSoup(response.text, 'lxml')
csrf = soup.find(attrs={"name": "_csrf"})['value']
data = {
    '_csrf': csrf,
    'LoginForm[username]': '17605888676', 
    'LoginForm[password]': 'ybb2601169057'
}

headers = {
    "Accept": "*/*",
    "DNT": "1",
    "Accept-Language": "zh",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _csrf=eea2f7088c1908de215a2e78f10d38f75f54966d2cc5aec97139fdf140f24ceda%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%2224ej1-kFkUaVc-x-Eavz0UQPviWB39CL%22%3B%7D; PHPSESSID=u0afeallurn6vacjate89d1p86; Hm_lvt_0280ecaa2722243b1de4829d59602c72=1558850537,1558859130; Hm_lpvt_0280ecaa2722243b1de4829d59602c72=1558859130",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://passport.21cnjy.com",
    "Referer": "https://passport.21cnjy.com/login?jump_url=",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

response = requests.post(url='https://passport.21cnjy.com/login?jump_url=', data=data, headers=headers)

print(response.text)
