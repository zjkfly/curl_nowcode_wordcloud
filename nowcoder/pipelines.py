# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class NowcoderPipeline(object):
    def __init__(self):
        self.f = open('te_pipline_employee.json', 'w')
        # 处理itcaast返回的数据

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.f.write(content)
        # 返回引擎，告诉他已经处理完了，继续下一个
        return item

    def close_spider(self, spider):
        self.f.close()

