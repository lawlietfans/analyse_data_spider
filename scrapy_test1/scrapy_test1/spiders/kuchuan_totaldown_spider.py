# -*- coding: utf-8 -*-
import scrapy
import json, traceback
from scrapy_test1.items import InfoItem
from scrapy_test1.utils.mylog import write2log
import time
from scrapy_test1.utils import get_config_list


class DownSpider(scrapy.Spider):
    name = 'kuchuan_totaldown_spider'
    allowed_domains = ['kuchuan.com']

    def start_requests(self):
        pkgs = get_config_list('app_pkg_name.txt')
        urlprefix = 'http://android.kuchuan.com/totaldownload?packagename='
        for p in pkgs:
            yield scrapy.Request(url=urlprefix + p, callback=self.parse)

    def parse(self, response):
        it = InfoItem()
        it['spider_name'] = self.name
        try:
            text = json.loads(response.text)
            it['results'] = {
                'pkgname': response.url.split('name=')[-1],
                'tick': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                'data': self.getDowndata(text['data'])
            }
        except Exception as e:
            traceback.print_exc()
            write2log(e)
            it['results'] = {}
        yield it

    def getDowndata(self, d):
        assert isinstance(d, dict)
        res = {}
        res['all'] = sum([i for i in d.values()])
        marketlist = get_config_list('market.txt')
        from scrapy_test1.utils import marketmapper
        for m in marketlist:
            res[m] = d[ marketmapper[m] ]
        return res
