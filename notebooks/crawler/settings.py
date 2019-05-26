# -*- coding: utf-8 -*-


BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = False

LOG_LEVEL = "ERROR"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"

ITEM_PIPELINES = {
   'crawler.pipelines.InfoPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
# 'crawler.middlewares.ProxyMiddleware': 543
}

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
RETRY_TIMES = 1
RETRY_ENABLED = True
DOWNLOAD_TIMEOUT = 300

# LOG_FILE = './logs/scrapy.log'