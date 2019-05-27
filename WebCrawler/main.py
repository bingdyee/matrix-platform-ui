# -*- coding: utf-8 -*-
import re
import json
import requests
import optparse
from bs4 import BeautifulSoup
from urllib.parse import urlencode, unquote


LOGIN_HEADERS = {
    'Origin': 'https://passport.21cnjy.com', 
    'Host': 'passport.21cnjy.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://passport.21cnjy.com/login',
}


template = '''
<!DOCTYPE html>
<html>
<head>
    <title>paper</title>
    <meta charset="utf-8">
    <style>
    
    </style>
</head>
<body>
<center><h3 style="">未经允许，不许复印和扫描！汇编作品著作权归宁波爻木心生物科技有限公司所有！</h3></center>
<ol class="content">
{}
</ol>
</body>
</html>
'''

option_template = '<span style="line-height:24px;float:left;width:220px;"><span>{}. </span><span>{}</span></span>'
li_template = '<li><div style="display:table-cell;padding-bottom: 20px;">{}</div></li>'
blank = '<span style="width: 80px;display: inline-block;border-bottom: 1px solid #000;vertical-align: baseline;text-align: center;"></span>'
login_url = 'https://passport.21cnjy.com/login'
fetch_url = 'https://zujuan.21cnjy.com/api/question/get-basket?xd=2&chid=3&pid={}&_timestamp=1558837017032&_=1558837016800'


def login(name, pwd, url=login_url):
    session = requests.session()
    response = session.get(url=url)
    csrf = BeautifulSoup(response.text, 'lxml').find(attrs={"name": "_csrf"})['value']
    data = {'_csrf': csrf, 'LoginForm[username]': name, 'LoginForm[password]': pwd}
    response = session.post(url=url, data=data, headers=LOGIN_HEADERS)
    login_result = json.loads(response.text)
    return session if login_result['errcode'] == 0 else None


def fetch(pid, session):
    if pid is None or session is None:
        print('Account or password error, login failed!')
        quit(0)
    response = session.get(fetch_url.format(pid))
    result = json.loads(response.text)
    return result['data']['content']


def parse_detail(questions):
    block = ''
    for question in questions:
        question_text = '<div>{}</div><br/>'.format(question['question_text'])
        options = question['options']
        if options:
            ops = ''.join([option_template.format(k, v) for k, v in options.items()])
            question_text += '<div>{}</div>'.format(ops)
        lists = question['list'] if question.get('list') else ''
        question_text += '<ol style="font-size:13px;">{}</ol>'.format(parse_detail(lists)) if lists else ''
        block += li_template.format(question_text)
    return re.sub('{#blank#}\d{#/blank#}', blank, block) 


def parse(contents):
    _template = '<li><h5>{}</h5><ol>{}</ol></li>'
    html = ''.join([_template.format(content['head_title'], parse_detail(content['questions'])) for content in contents])
    return template.format(html)
   

def main():
    parser = optparse.OptionParser("usage: %prog -P <pid> [-u <username> -p <password>]")
    parser.add_option("-P", '--pid', dest="pid", type="string", help="specify paper pid")
    parser.add_option("-u", '--username', dest="username", type="string", help="specify username", default='')
    parser.add_option("-p", '--password', dest="password", type="string", help="specify password", default='')
    options, args = parser.parse_args()
    if options.pid is None:
        print(parser.print_help())
    else:
        username = DEFAULT_USERNAME if options.username is None else options.username
        password = DEFAULT_PASSWORD if options.password is None else options.password
        session = login(username, password)
        html = parse(fetch(options.pid, session))
        with open('{}.html'.format(options.pid), 'w', encoding='utf-8') as pf:
            pf.write(html)
        print('Finished!>> {}.html'.format(options.pid))


if __name__ == '__main__':
    main()