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