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
import argparse
from bs4 import BeautifulSoup
import json
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

def fetch(opts, idx, opt):
    result = ''
    try:
       result =  '<strong>'+ opt +'</strong>. ' + str(opts[idx]['options'][opt])
    except:
        pass
    return result

blank = '<span style=\'width: 80px;display: inline-block;border-bottom: 1px solid #000;vertical-align: baseline;text-align: center;\'></span>'

def parse(subject):
    title = subject['head_title']
    questions = subject['questions']
    txt = ''
    for question in questions:
        question_text = question['question_text']
        options = question['options']
        li = '<li><div>{}</div>{}</li><br>'
        opt = ''
        if 'list' not in question.keys() and len(options) > 2 and (title == '单选题' or title == '多选题'):
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

        if 'list' in question.keys() and len(question['list']) > 0:
            _list = question['list']
            for i in range(len(_list)):
                if _list[i]['question_type'] != '2':
                    opt += '<p>({}).&nbsp;&nbsp;{}</p>'.format(i + 1, _list[i]['question_text'])
                else:
                    ans = '<div><span>{} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><span> {}&nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} &nbsp;&nbsp;&nbsp;&nbsp;</span><span> {} </span></div>'.format(
                        fetch(_list, i, 'A'), fetch(_list, i, 'B'),
                        fetch(_list, i, 'C'), fetch(_list, i, 'D'), fetch(_list, i, 'E'))
                    opt += '<p>({}).&nbsp;&nbsp;{}</p>'.format(i + 1, _list[i]['question_text'], _list[i]['options']) + ans
        txt += li.format(question_text, opt)
    txt = '<h5> {}</h5>\n<ol>{}</ol>\n'.format(title, txt)
    return re.sub('{#blank#}\d{#/blank#}', blank, txt)

def main_func(kemu,pid,cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie': cookie
    }
    url = 'https://www.zujuan.com/paper/viewuser-' + pid + '.shtml'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    extract = re.findall(r'var MockDataTestPaper =(.*)[;]', str(soup))
    extract = re.sub('<input.{1,120}/>', blank, extract[0])
    data = json.loads(extract)
    print('Yomursin成功为您导出试卷~_~')
    print('非常感谢余斌斌程序猿的指导！！！')
    html_name = 'Yomursin教育——' + kemu + '.html'
    with open(html_name, 'w', encoding='utf-8') as pf:
        content = ''
        for subject in data:
            rs = parse(subject)
            content += rs
        pf.write('<strong>Yomursin教育——</strong>' + kemu)
        pf.write(template.format(content))

