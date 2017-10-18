# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ACCll 报错信息解决方案
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import json
import csv


class DouyuJsonPipeline(object):
    # pass
    def __init__(self):
        self.file = open('Douyu.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()


class DouyuCSVPipeline(object):

    def __init__(self):
        self.csvwriter = csv.writer(open('Douyu.csv', 'wb'), delimiter=',')
        self.cs = 1
    def process_item(self, item, spider):

        data_list=item.values()
        if self.cs == 1:
            self.csvwriter.writerow(item.keys())
            self.cs += 1

        self.csvwriter.writerow(data_list)



        # self.csvwriter.writerow(item['zb_fjmc'], item['zb_zbmc'], item['zb_yxlx'], item['zb_gkrs'])

        return item
