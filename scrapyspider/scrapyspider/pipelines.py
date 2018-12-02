# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ScrapyspiderPipeline(object):

    def __init__(self):
        self.fb = open("yf.json", "w", encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始。。')

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fb.write(item_json + '\n')
        return item

    def close_spider(self, spider):
        self.fb.close()
        print('爬虫结束。。。')
