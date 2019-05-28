# -*- coding:utf-8 -*-
"""
Copyleft 2018 The Tools Authors. All Rights Reserved.
https://zujuan.21cnjy.com/login
    LoginForm[username]: 17605888676
    LoginForm[password]: ybb2601169057
    _csrf: 
    LoginForm[rememberMe]: 1

https://zujuan.21cnjy.com/paper/detail?pid=1097617&_=1532316884540
@Author: Aaron Vu
@Date: 2018/7/11/011
@Email: fetaxyu@gmail.com
======================================================="""
import re
import time
import requests
from bs4 import BeautifulSoup
from zujuan_main import main_func, fetch
template = '''
<!DOCTYPE html>
<html>
<head>
    <title>paper</title>
    <meta charset="utf-8">
    <style></style>
</head>
<body>
<h5>未经允许，不许复印和扫描！汇编作品著作权归宁波爻木心生物科技有限公司所有！</h5>
<div class="content">
{}
</div>
</body>
</html>
'''
kemu = input('科目:')
pid = input("pid:")
cookie = input("cookie:")
logo = '<strong>Yomursin教育——</strong>'+ kemu

# kemu = '1'
# pid = '1167716'
# cookie = 'UM_distinctid=16474f5adb5d57-020e2328d4e652-4446062d-1fa400-16474f5adb69f8; _qddaz=QD.gitbvc.ew1d2p.jjwxwzs9; HqNL_ef65_saltkey=i3N3vm4Z; HqNL_ef65_lastvisit=1533457620; Hm_lvt_0280ecaa2722243b1de4829d59602c72=1530970615,1533461216; OUTFOX_SEARCH_USER_ID_NCOO=92197554.67391792; _sync_login_identity=926277beb2fe9d7133ea8a784c946a9d7491ee53d8790d5ad73ee972b25710f4a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B8697152%2C%22tnhPe0vzjmB98Sc4AMc8BxSFrCrxmauO%22%2C86400%5D%22%3B%7D; PHPSESSID=q9vau894kvmb2jfmt2vfkfjaq5; _identity=cba16fdf207006ab1c20bf7f4f2424547fcb996131143db634d1ea3e0a762294a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B8697152%2C%222009414b791556e6b63ae48c1e997c11%22%2C86400%5D%22%3B%7D; _csrf=34c3ebce656ef9ec1a9ff41601fec766ea49157c9fe0a29d7b96bb25f4831304a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22T0IXSGNwJq4Yto46BF4pktPI5sjw2aK6%22%3B%7D; Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef=1534745970,1534754994,1534830568,1534849579; chid=bd6891efb02e2089ca240a76027e7059a83f5f17127ff3702e5715f697e4b64ca%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%225%22%3B%7D; xd=053c08991644b3be1f1cce76412b1634d2eb9867b529f5e7d3129bc291581e9ba%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%222%22%3B%7D; Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef=1534850763'
# logo = '<strong>Yomursin教育——</strong>'+ kemu

def parse(subject):
    title = subject['head_title']
    questions = subject['questions']
    txt = ''
    blank = '<span style=\'width: 80px;display: inline-block;border-bottom: 1px solid #000;vertical-align: baseline;text-align: center;\'></span>'
    for question in questions:
        question_text = question['question_text']
        options = question['options']
        _list = question['list']
        li = '<li><div>{}</div>{}</li><br>'
        opt = ''
        if title == '单选题' or title == '多选题':
            num = []
            for key in options:
                chi = re.findall(r'[\u4E00-\u9FFF]', options[key])
                num.append(len(chi))
            if max(num) <= 13:
                opt = '<div><span><br>{} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} </span></div>'.format(
                    '<strong>A</strong>. ' + str(options['A']), '<strong>B</strong>. ' + str(options['B']),
                    '<strong>C</strong>. ' + str(options['C']), '<strong>D</strong>. ' + str(options['D']))
            if max(num) > 13 and max(num) <= 25:
                opt = '<div><span><br>{} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><br><span> {} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} </span></div>'.format(
                    '<strong>A</strong>. ' + str(options['A']), '<strong>B</strong>. ' + str(options['B']),
                    '<strong>C</strong>. ' + str(options['C']), '<strong>D</strong>. ' + str(options['D']))
            if max(num) > 25:
                opt = '<div><span><br>{} &nbsp;&nbsp;&nbsp;&nbsp;</span><br><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><br><span> {} &nbsp;&nbsp;&nbsp;&nbsp;</span><br><span> {} </span></div>'.format(
                    '<strong>A</strong>. ' + str(options['A']), '<strong>B</strong>. ' + str(options['B']),
                    '<strong>C</strong>. ' + str(options['C']), '<strong>D</strong>. ' + str(options['D']))

        if _list and len(_list) > 0:
            for i in range(len(_list)):
                if _list[i]['question_type'] != '1'and _list[i]['question_type'] != '2':
                    opt += '<p>({}).&nbsp;&nbsp;{}</p>'.format(i + 1, _list[i]['question_text'])
                else:
                    ans = '<div><span>{} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} </span></div>'.format(
                    fetch(_list, i, 'A'), fetch(_list, i, 'B'),
                    fetch(_list, i, 'C'), fetch(_list, i, 'D'), fetch(_list, i, 'E'))
                    opt += '<p>({}).&nbsp;&nbsp;{}</p>'.format(i + 1, _list[i]['question_text'], _list[i]['options']) + ans
        txt += li.format(question_text, opt)
    txt = '<h5> {}</h5>\n<ol>{}</ol>\n'.format(title, txt)
    return re.sub('{#blank#}\d{#/blank#}', blank, txt)

def main(pid):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie': cookie
    }
    response = requests.get('https://zujuan.21cnjy.com/paper/detail?pid={}&_={}'.format(pid, int(time.time()*1000)), headers=headers)
    print('Yomursin成功为您导出试卷~_~')
    print('非常感谢余斌斌程序猿的指导！！！')
    data = response.json()
    html_name = 'Yomursin教育——'+ kemu + '.html'
    # ids = data['_meta']['question_ids']
    # for id in ids:
    #     url = 'https://zujuan.21cnjy.com/question/detail/'+id
    #     response = requests.get(url, headers=headers)
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     print(soup)

    with open(html_name, 'w', encoding='utf-8') as pf:
        content = ''
        for subject in data['content']:
            rs = parse(subject)
            content += rs
        pf.write(logo)
        pf.write(template.format(content))

if __name__ == '__main__':
    if input('来源:') == '1':
        main(pid)
    else:
        main_func(kemu, pid, cookie)
