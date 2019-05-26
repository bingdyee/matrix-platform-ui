# -*- coding: utf-8 -*-
import scrapy
from crawler.items import BaseItem

class BaseSpider(scrapy.Spider):

    name = 'spider'
    start_urls = ['https://passport.21cnjy.com/login?jump_url=https%3A%2F%2Fzujuan.21cnjy.com%2F']

    # def start_requests(self):
    #     scrapy.FormRequest()
    #     # yield scrapy.Request(url="", callback=self.parse, meta={'pid': 0}, dont_filter=True)

    def parse(self, response):
        '''
        csrf = response.xpath("//input[@name='_csrf']/@value").extract_first()
        post_data = {
            "_csrf": csrf, 
            'LoginForm[username]': '17605888676',
            'LoginForm[password]': 'ybb2601169057',
            'LoginForm[rememberMe]': '0'
        }
        yield scrapy.FormRequest(start_urls[0], formdata=post_data, callback=self.after_login)
        '''
        yield scrapy.FormRequest.from_response(
            response, 
            formdata={'LoginForm[username]': '17605888676', 'LoginForm[password]': 'ybb2601169057'}, 
            callback=self.after_login
        )

    def after_login(self, response):
        print(response.body.decode())

    def parse_detail(self, response):
        item = BaseItem()
        item['pid'] = response.meta['pid']
        yield item



