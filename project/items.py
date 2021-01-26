# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_world = scrapy.Field()
    posttion_place = scrapy.Field()
    posttion_led = scrapy.Field()
    position_department = scrapy.Field()
    positon_time = scrapy.Field()
    position_info = scrapy.Field()


class hupu_articles(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class hupu_light(scrapy.Item):
    #引用内容
    hupu_light_appoint = scrapy.Field() #//*[@id="readfloor"]/div[1]/div[2]/table/tbody/tr/td/blockquote
    #亮评
    hupu_light_better = scrapy.Field()#//*[@id="readfloor"]/div[1]/div[2]/table/tbody/tr/td   -   article_appoint
    #点亮数
    hupu_light_num = scrapy.Field() #//*[@id="readfloor"]/div[1]/div[2]/div/div/span/span/span/text()


class hupu(scrapy.Item):
    article_name = scrapy.Field()
    article_content = scrapy.Field()
    article_comment = []

