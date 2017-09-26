# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from house_spider.items import HouseSpiderItem
from house_spider.util.mongoutil import MongoSinleton

class HouseSpiderPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        MongoSinleton.singleton().open_db()
        pass

    def close_spider(self, spider):
        MongoSinleton.singleton().close_db()
        pass

    def process_item(self, item, spider):
        MongoSinleton.singleton().insert_db(MongoSinleton.singleton().collection, dict(item))
        return item
