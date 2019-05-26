# -*- coding: utf-8 -*-
import random
import requests


class ProxyMiddleware(object):

    proxy_url = 'http://api3.xiguadaili.com/ip/?tid=557957240942494&protocol=https&num=50'
    proxy_pool = []

    @staticmethod
    def fetch_proxy():
        r = requests.get(ProxyMiddleware.proxy_url)
        ProxyMiddleware.proxy_pool = ['https://{}'.format(str(ip, encoding="utf8")) for ip in r.iter_lines()]
        print(ProxyMiddleware.proxy_pool)

    @staticmethod
    def randip():
        return ProxyMiddleware.proxy_pool[random.randint(0, len(ProxyMiddleware.proxy_pool) - 1)]

    def process_request(self, spider, request):
        if len(ProxyMiddleware.proxy_pool) < 1:
            ProxyMiddleware.fetch_proxy()
        request.meta['proxy'] = ProxyMiddleware.randip()