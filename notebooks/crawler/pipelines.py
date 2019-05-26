# -*- coding: utf-8 -*-



class InfoPipeline(object):

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        pass