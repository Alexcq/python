# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myzbxx(scrapy.Item):
    #ֱ直播房间名称
    zb_fjmc =scrapy.Field()
    #直播地址
    zb_url = scrapy.Field()
    #直播-主播名称
    zb_zbmc = scrapy.Field()
    #直播-类型
    zb_yxlx = scrapy.Field()
    #观看人数
    zb_gkrs = scrapy.Field()
