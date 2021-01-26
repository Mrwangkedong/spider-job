# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ProjectPipeline(object):
    def __init__(self):
        print('实例化DemoPipeline')
        self.f = open('itcast_pipeline1.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.f.write(content)
        print(content)
        return item

    # 结束后做的操作，在这里我们要关闭文件
    def close_spider(self, spider):
        print('结束')
        self.f.close()
