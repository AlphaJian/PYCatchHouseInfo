# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    size = scrapy.Field()
    location_district = scrapy.Field()
    location_area = scrapy.Field()
    location_detail = scrapy.Field()
    unitprice = scrapy.Field()
    totalprice = scrapy.Field()
    tag = scrapy.Field()
    year = scrapy.Field()

    _id = scrapy.Field()
    priceLog = scrapy.Field()

    def parse_self_to_dict(self):
        return {"title": self["title"],
                "size": self["size"],
                "location_district": self["location_district"],
                "location_area": self["location_area"],
                "location_detail": self["location_detail"],
                "year": self["year"]}

    def parse_dict_to_self(self, dict):
        self["title"] = dict["title"]
        self["size"] = dict["size"]
        self["location_district"] = dict["location_district"]
        self["location_area"] = dict["location_area"]
        self["location_detail"] = dict["location_detail"]
        self["unitprice"] = dict["unitprice"]
        self["totalprice"] = dict["totalprice"]
        self["tag"] = dict["tag"]
        self["year"] = dict["year"]
        self["_id"] = dict["_id"]
        self["priceLog"] = dict["priceLog"] if dict.has_key("priceLog") else None
