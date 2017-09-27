# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseSpiderItem
from house_spider.util.utility import StringUtil

class HouseSpider(scrapy.Spider):
    name = "house-spider"
    start_urls = ["http://sh.lianjia.com/ershoufang/pudong/a4l3"]

    host_url = "http://sh.lianjia.com"

    def parse(self, response):
        model = HouseSpiderItem()
        for item in response.xpath("//ul[@class='js_fang_list']//div[@class='info']"):
            model['title'] = item.xpath(".//a[@class='text link-hover-green js_triggerGray js_fanglist_title']/text()").\
                extract_first().encode("utf-8")
            model['location_district'] = item.xpath(".//span[@class='info-col row2-text']/a[2]/text()").extract_first().\
                encode("utf-8")
            model['location_area'] = item.xpath(".//span[@class='info-col row2-text']/a[3]/text()").extract_first().\
                encode("utf-8")
            model['location_detail'] = item.xpath(".//span[@class='info-col row2-text']/a[1]/span/text()").extract_first().\
                encode("utf-8")

            model['totalprice'] = item.xpath(".//span[@class='total-price strong-num']/text()").extract_first().encode("utf-8") +\
                                  item.xpath(".//span[@class='unit']/text()").extract_first().encode("utf-8")
            unitprice_info = item.xpath(".//span[@class='info-col price-item minor']/text()").extract_first().encode("utf-8")
            model['unitprice'] = StringUtil.remove_space(unitprice_info)
            house_info = item.xpath(".//span[@class='info-col row1-text']").xpath("string(.)").extract_first().encode("utf-8")
            model['size'] = StringUtil.remove_space(house_info).split("|")[1]
            year_info = item.xpath(".//span[@class='info-col row2-text']").xpath("string(.)").extract_first().encode("utf-8")
            model['year'] = self.catch_year(year_info)
            list_tag = item.xpath(".//div[@class='property-tag-container']/span")
            model['tag'] = self.split_tagitems(list_tag)

            model['priceLog'] = {}
            yield model


        next_page_url = response.xpath("//a[@gahref='results_next_page']/@href").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(self.host_url + next_page_url.encode("utf-8"))

    def split_tagitems(self, selector):
        taglist = []
        for item in selector:
            taglist.append(str(item.xpath("./text()").extract_first().encode("utf-8")))
        return taglist

    def catch_year(self, year_info):
        liststr = StringUtil.remove_space(year_info).split("|")
        if len(liststr) == 4:
            return StringUtil.fetch_number(liststr[3])