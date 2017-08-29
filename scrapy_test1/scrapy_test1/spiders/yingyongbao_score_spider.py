# encoding: utf-8
__author__ = 'fengshenjie'
import scrapy
from scrapy_test1.utils import get_pkg_list
from scrapy_test1.items import InfoItem
from scrapy_test1.utils.mylog import write2log
from lxml import etree
import traceback, time


class YingyongbaoScore(scrapy.Spider):
    name = 'yingyongbao_score_spider'

    def start_requests(self):
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'sj.qq.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
        }
        prefixurl = 'http://sj.qq.com/myapp/detail.htm?apkName='
        pkglist = get_pkg_list()
        urls = [prefixurl + i for i in pkglist]
        for u in urls:
            yield scrapy.Request(url=u, headers=header)

    def parse(self, response):
        results = {
            'pkgname' : response.url.split('apkName=')[-1],
            'date': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            'market': 'yingyongbao',
        }
        page = etree.HTML(response.text)
        try:
            results['score']=float(page.xpath("//div[@class='com-blue-star-num']")[0].text[:-1])
        except Exception as e:
            traceback.print_exc()
            write2log('抓取score失败'+e)

        yield InfoItem({
            'results': results,
            'spider_name': self.name
        })
