# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class LagouMongoDBPipeline(object):
    def __init__(self):
        # 创建MongoDB数据库连接
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        # 指定MongoDB的数据库名
        self.db_name = self.client['Lagou']
        # 指定数据库表名
        self.sheet_name = self.db_name['LagouINFO2']

    def process_item(self, item, spider):
        # 向表里插入数据，参数是一个字典
        self.sheet_name.insert(dict(item))
        return item

