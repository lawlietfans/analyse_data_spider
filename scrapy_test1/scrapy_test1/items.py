# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    results = scrapy.Field()
    # 根据更新频率（抓取频率）来划分spider，
    # apps/version/     app_info
    # download      down_info
    # comment/score     comment_info
    spider_name = scrapy.Field()


if __name__ == '__main__':
    d={'results':0, 'spider_name':'s'}
    x=InfoItem(d)
    print(x)