# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.http.request import Request
from LagouScrapy.items import LagouzhiweiInFo
import re


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com']
    headers = {
        # 反爬点1：检查Referer是否是正常合理的Referer
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        # 反爬点2：检查User-Agent
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Cookie": "user_trace_token=20171023214920-f84ccc1f-b7f8-11e7-a585-525400f775ce; LGUID=20171023214920-f84cd024-b7f8-11e7-a585-525400f775ce; isCloseNotice=0; _gid=GA1.2.2117655637.1508766557; ab_test_random_num=0; index_location_city=%E6%B7%B1%E5%9C%B3; _gat=1; login=false; unick=""; JSESSIONID=ABAAABAAAHAAAFD8D5D14F2736575842FCD40D96B72512E; _putrc=""; _ga=GA1.2.2109036961.1508766557; X_HTTP_TOKEN=becedc2c2152abc5a5686b9659c86913; _ga=GA1.3.2109036961.1508766557; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508856495,1508890962,1508919906,1508930402; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1508932887; LGSID=20171025192008-75601a80-b976-11e7-9617-5254005c3644; LGRID=20171025200133-3e948f16-b97c-11e7-9617-5254005c3644; ticketGrantingTicketId=_CAS_TGT_TGT-3d15ad0c514a4a16bd4104ff04b526bb-20171025200144-_CAS_TGT_"

    }

    def parse(self, response):
        # 获取主页中所有职位url
        zw_url = response.xpath('//div[@class="menu_sub dn"]/dl/dd/a/@href').extract()

        # yield Request(zw_url[0], headers=self.headers, callback=self.parse_zw)
        for url in zw_url:
            yield Request(url, headers=self.headers, callback=self.parse_zw)

    def parse_zw(self, response):
        # 获取单个职位信息中全国职位
        dgzw_url = response.xpath('//div[@class="p_top"]/a/@href').extract()

        # 拿出每个页面中招聘url
        for url in dgzw_url:
            # print(url)
            time.sleep(1)
            yield Request(url, headers=self.headers, callback=self.parse_info)
        # 查看是否有下一页
        try:
            next_url = response.xpath('//div[@class="item_con_pager"]/div/a/@href').extract()
            if next_url[-1] != "javascript:;":
                yield Request(next_url[-1], headers=self.headers, callback=self.parse_zw)
        except:
            print("没有下一页")

    def parse_info(self, response):
        # 职位详情页面
        print("职位详情页面 " + response.url)
        item = LagouzhiweiInFo()

        # 公司名称
        item["gs_mc"] = response.xpath('//div[@class="job-name"]/div[1]/text()').extract()
        # 职位名称
        item["zwmc"] = response.xpath('//div[@class="job-name"]/span/text()').extract()[0]
        # 职位工资
        item["zw_gz"] = response.xpath('//dd[@class="job_request"]/p/span[1]/text()').extract()[0]
        # 职位地点
        item["zw_dd"] = response.xpath('//dd[@class="job_request"]/p/span[2]/text()').extract()[0][1:-1]
        # item["zw_dd"] =re.findall(r'[\u4e00-\u9fa5\d-]+',str(dd),re.S)[0]
        # 经验要求
        item["zw_jyyq"] = response.xpath('//dd[@class="job_request"]/p/span[3]/text()').extract()[0][:-2]
        # 学历要求
        item["zw_xl"] = response.xpath('//dd[@class="job_request"]/p/span[4]/text()').extract()[0][:-1]
        # 职位类型
        item["zw_lx"] = response.xpath('//dd[@class="job_request"]/p/span[5]/text()').extract()[0]
        # 职位关键字
        item["zw_gjz"] = response.xpath('//dd[@class="job_request"]/ul/li/text()').extract()
        # 职位诱惑
        item["zw_yh"] = response.xpath('//dd[@class="job-advantage"]/p/text()').extract()[0]
        # 职位描述
        item["zw_ms"] = response.xpath('//dd[@class="job_bt"]/div/p/text()').extract()
        # 工作地址 要去空格
        try:

            s = response.xpath('//div[@class="work_addr"]/text()').extract()
            s1 = re.findall(r'[\u4e00-\u9fa5\d]+', str(s), re.S)
            y = response.xpath('//div[@class="work_addr"]/a/text()').extract()
            s2 = ""
            for i in y:
                s2 += i
            # print(s1)
            item["gz_dz"] = s2[:-4] + s1[0]
        except:
            item["gz_dz"] = "None"
        # 公司类型
        lx = response.xpath('//ul[@class="c_feature"]/li[1]/text()').extract()
        item["gs_lx"] = re.findall(r'[\u4e00-\u9fa5\d-]+', str(lx), re.S)[0]
        # 公司情况
        item["gs_qk"] = response.xpath('//ul[@class="c_feature"]/li[2]/text()').extract()[1]
        # item["gs_qk"] = re.findall(r'[\u4e00-\u9fa5\d-]+',str(qk),re.S)[0]
        # 公司人数
        item["gs_rs"] = response.xpath('//ul[@class="c_feature"]/li[3]/text()').extract()
        # item["gs_rs"] = re.findall(r'[\w\u4e00-\u9fa5\d-]+',str(d),re.S)
        # 公司网站
        item["gs_url"] = response.xpath('//ul[@class="c_feature"]/li/a/text()').extract()[0]

        # # print(item)
        yield item
