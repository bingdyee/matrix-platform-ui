# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WebcrawlerPipeline(object):

    def process_item(self, item, spider):
        if item['code'] != 0:
            return None
        contents = item['data']['content']
        for content in contents:
            title = content['head_title']
            questions = content['questions']
            print(questions)
        return item
