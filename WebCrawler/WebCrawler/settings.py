# -*- coding: utf-8 -*-

# Scrapy settings for WebCrawler project

BOT_NAME = 'WebCrawler'

SPIDER_MODULES = ['WebCrawler.spiders']
NEWSPIDER_MODULE = 'WebCrawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = "ERROR"
LOG_FILE = 'scrapy.log'

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"

# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7',
# }


# Enable or disable spider middlewares
ITEM_PIPELINES = {
   'WebCrawler.pipelines.WebcrawlerPipeline': 300,
}

# SPIDER_MIDDLEWARES = {
#    'WebCrawler.middlewares.WebcrawlerSpiderMiddleware': 543,
# }

# # Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#    'WebCrawler.middlewares.WebcrawlerDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

COOKIES_ENABLED = True
# COOKIES_DEBUG = True

# DOWNLOAD_DELAY = 1
# RANDOMIZE_DOWNLOAD_DELAY = True
# RETRY_TIMES = 1
# RETRY_ENABLED = True
# DOWNLOAD_TIMEOUT = 300


REDIRECT_ENABLED = True
HTTPERROR_ALLOWED_CODES = [302, 400]

