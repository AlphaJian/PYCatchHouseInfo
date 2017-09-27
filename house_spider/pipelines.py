# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from house_spider.items import HouseSpiderItem
from house_spider.util.mongoutil import MongoSinleton
from house_spider.util.utility import StringUtil
class HouseSpiderPipeline(object):

    collection = None

    def __init__(self):
        pass

    def open_spider(self, spider):
        self.collection = MongoSinleton.singleton().open_db()
        pass

    def close_spider(self, spider):
        MongoSinleton.singleton().close_db()
        pass

    def process_item(self, item, spider):
        find_dict = MongoSinleton.singleton().findone_db(self.collection, item.parse_self_to_dict())
        new_item = HouseSpiderItem()
        find_key = {}
        if find_dict is not None:
            find_key = {"_id": find_dict["_id"]}
            new_item.parse_dict_to_self(find_dict)
            updated_dict = self.update_price_log(new_item)
            if updated_dict is not None:
                new_item["priceLog"] = updated_dict
                MongoSinleton.singleton().update_db(self.collection, find_key, dict(new_item))
            else:
                # No need to update
                return new_item

        else:
            new_item = item
            new_item["priceLog"] = self.update_price_log(item)
            MongoSinleton.singleton().insert_db(self.collection, dict(new_item))

        return new_item

    def update_price_log(self, item):
        dict = {}
        time_key = StringUtil.get_str_today()
        time_key = "2017-09-09"
        if item["priceLog"] is not None:
            dict = item["priceLog"]
            if dict.has_key(time_key) is False:
                dict[time_key] = item["totalprice"]
            else:
                return None
        else:
            dict = {time_key: item["totalprice"]}

        return dict