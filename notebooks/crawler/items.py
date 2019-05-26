# -*- coding: utf-8 -*-
import scrapy


class BaseItem(scrapy.Item):
    pid = scrapy.Field()