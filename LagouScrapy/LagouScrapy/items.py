# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouscrapyItem(scrapy.Item):
    # 职位类型 和url
    zwlx = scrapy.Field()
    zwlx_url = scrapy.Field()

    #工作地点和url
    gzcs = scrapy.Field()
    gzcs_url = scrapy.Field()


class LagouzhiweiInFo(scrapy.Item):
    # 职位信息
    # 公司名称
    gs_mc = scrapy.Field()
    #职位名称
    zwmc = scrapy.Field()
    # 职位工资
    zw_gz = scrapy.Field()
    # 职位地点
    zw_dd = scrapy.Field()
    # 经验要求
    zw_jyyq = scrapy.Field()
    # 学历要求
    zw_xl = scrapy.Field()
    # 职位类型
    zw_lx = scrapy.Field()
    # 职位关键字
    zw_gjz = scrapy.Field()
    # 职位诱惑
    zw_yh = scrapy.Field()
    # 岗位职责
    zw_ms = scrapy.Field()
    # 任职要求
    rz_yq = scrapy.Field()
    # 工作地址
    gz_dz = scrapy.Field()


    # 公司类型
    gs_lx = scrapy.Field()
    # 公司情况
    gs_qk = scrapy.Field()
    # 公司人数
    gs_rs = scrapy.Field()
    # 公司网站
    gs_url = scrapy.Field()


