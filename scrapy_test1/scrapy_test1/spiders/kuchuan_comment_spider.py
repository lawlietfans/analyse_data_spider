# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_test1 import utils


class KuchuanComment(scrapy.Spider):
    name = 'kuchuan_comment_spider'
    allowed_domains = ['kuchuan.com']

    def start_requests(self):
        pkglist=utils.get_pkg_list()
        marketlist=utils.get_config_list('market.txt')
        url='http://android.kuchuan.com/commentdetail?packagename=com.zl.fqbao&market=360&score=1%2C2%2C3%2C4%2C5&index=1&count=20&date=1503389056771'


    def parse(self, response):
        pass

if __name__ == '__main__':
    pass
