# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy_test1.utils import get_pkg_list

class AppSpider(scrapy.Spider):
    name = 'app_info_spider'
    allowed_domains = ['kuchuan.com']
    # package / name / company / developer
    # despcription

    def start_requests(self):
        pkglist=get_pkg_list()
        prefix_kuchuan='http://android.kuchuan.com/totaldownloud?packagename='
        start_urls = []

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        prefix_sjqq = 'http://sj.qq.com/myapp/detail.htm?apkName='
        print(res)
        yield {'totaldownload':res}

    def parse_app(self, response):
        pass

'''
{'appinfo':{},
'versioninfo':[]
}
'''
