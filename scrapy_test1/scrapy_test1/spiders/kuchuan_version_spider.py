# encoding: utf-8
__author__ = 'fengshenjie'
import scrapy
from scrapy_test1.utils import get_config_list, findby_re
from scrapy_test1.items import InfoItem
import json, traceback
from scrapy_test1.utils.mylog import write2log

class KuchuanVersion(scrapy.Spider):
    name = 'kuchuan_version_spider'
    allowed_domains = ['kuchuan.com']

    def start_requests(self):
        pkglist = get_config_list('app_pkg_name.txt')
        # marketlist=get_config_list('market.txt')
        header = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Host': 'android.kuchuan.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        import time
        urls = []
        for pkg in pkglist:
            urls.append(
                'http://android.kuchuan.com/versiondetail?packagename={0}&market=yingyongbao&date={1}'.format(
                    pkg,
                    str(time.time()).split('.')[0]
                )
            )
        for u in urls:
            yield scrapy.Request(url=u, headers=header, cookies=self.getCookie())

    def parse(self, response):
        jpage = json.loads(response.text)
        if jpage['status'] is not 200:
            write2log(response.text)
        results = {
            "packagename": findby_re(r'name=(.*?)&', response.url),
            "data": jpage['data'],
        }
        yield InfoItem({
            'spider_name': self.name,
            'results': results
        })

    def getCookie(self):
        cookiestr='UM_distinctid=15de67a194f791-00c59ec69c123e-143a6d57-fa000-15de67a19503ee; _Coolchuan_com_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFRkkiJTlmM2M1OGRhMzkwNmM1ZmVkOGM3OTE2OGE0MWYzZjM5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUoxSkJvcUdvUXVGNEhqNlNwRjBFRDRmNFllZzBjRWJhWlQrZXNIZ1ZXR0k9BjsARg==--c1b0fcd79ba4a5b3eddfc9e527ed26d7a2208e55; uname=; uid=; bcelin=; uniqueId=5c2987f286c94b10a4c7083898d78374; JSESSIONID=wll6dv87x2bo1rtafwiih59ru; _gat=1; token=2cc87592c88ebe8980f4c9021ab90b69; sign=btLJdR4iWw4W0j7nNSprjDhcQOj9AAGgK%2FCtxN3zCBGKRS5z4UDaNSIRfqg3AevMmk26IyDV1x7ihI8FRRYNtcspii7BOgMkfPn3KOht%2BCokfPjxbM2YqRKk767ESD5F5bjHCQLllL%2BDiF1tYYFpDmT%2FtvziwgLfatMf3URp4IY%3D; CNZZDATA5103679=cnzz_eid%3D263761242-1502810302-http%253A%252F%252Fios.kuchuan.com%252F%26ntime%3D1503367124; CNZZDATA1260525360=391574454-1502807253-http%253A%252F%252Fios.kuchuan.com%252F%7C1503370750; CNZZDATA1257619731=883031219-1502810302-http%253A%252F%252Fios.kuchuan.com%252F%7C1503370750; _ga=GA1.2.345139532.1502810375; _gid=GA1.2.1712226620.1503278416'
        res={}
        for c in cookiestr.split('; '):
            t=c.split('=')
            res[t[0]]=t[1]
        return res
