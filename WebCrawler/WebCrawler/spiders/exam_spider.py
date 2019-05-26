# -*- coding: utf-8 -*-
import json
import scrapy
from urllib.parse import urlencode


class ExamSpider(scrapy.Spider):

    name = 'exam'
    allowed_domains = ['.21cnjy.com', 'passport.21cnjy.com', 'zujuan.21cnjy.com']
    login_url = 'https://passport.21cnjy.com/login'
    fetch_url = 'https://zujuan.21cnjy.com/api/question/get-basket?xd=2&chid=3&pid=&_timestamp=1558837017032&_=1558837016800'

    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login, meta={'cookiejar': 1})

    def login(self, response):
        # csrf = response.xpath("//input[@name='_csrf']/@value").extract_first()
        cookies = response.headers.getlist('Set-Cookie')
        req_cookie = response.request.headers.getlist('Cookie')
        headers = {
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
            'Cookie': response.meta['cookiejar']
        }
        yield scrapy.FormRequest.from_response(
            response, 
            formdata={
                'LoginForm[username]': '17605888676', 
                'LoginForm[password]': 'ybb2601169057',
            }, 
            meta={'cookiejar': True},
            callback=self.parse,
            dont_filter=True,
            headers=headers
        )

    def parse(self, response):
        yield scrapy.Request(
            url=self.fetch_url, 
            callback=self.parse_detail,
            meta={'cookiejar': True},
            dont_filter=True,
        )

    def parse_detail(self, response):
        print('*******************************')
        print('Result', response.body.decode())
        
