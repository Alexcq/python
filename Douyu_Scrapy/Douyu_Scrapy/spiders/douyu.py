# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douyu_Scrapy.items import Myzbxx
import re


class DouyuSpider(CrawlSpider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    start_urls = ['http://www.douyu.com/directory#']

    rules = (
        Rule(LinkExtractor(allow=r'www\.douyu\.com/directory/game/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        res = response.xpath(r'//ul[@class="clearfix play-list"]/li')
        itmes = []
        for zbxx in res:
            itme = Myzbxx()
            try:
                fjmc = zbxx.xpath('./a/div/div/h3/text()').extract()[0]
            except:
                fjmc = "  0   "
            zbmc = zbxx.xpath('./a/div/p/span[1]/text()').extract()[0]
            yx = zbxx.xpath('./a/div/div/span/text()').extract()[0]
            rs = zbxx.xpath('./a/div/p/span[2]/text()').extract()[0]
            url = zbxx.xpath('./a/@href').extract()[0]
            itme["zb_url"] = 'https://www.douyu.com' + url
            # for fj in fjmcs:
            itme["zb_fjmc"] = fjmc.strip()
            # for mc in zbmcs :
            itme["zb_zbmc"] = zbmc
            # for rs in rss:
            itme["zb_gkrs"] = rs
            # for yx in yxs
            itme["zb_yxlx"] = yx
            # print(fjmc,zbmc,yx,rs)
            # print(itme)
            # itmes.append(itme)

            yield itme
