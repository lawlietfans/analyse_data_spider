# encoding: utf-8
__author__ = 'fengshenjie'
# https://stackoverflow.com/questions/24875280/scrapy-cmdline-execute-stops-script

from twisted.internet import reactor

from scrapy import log, signals
from scrapy.crawler import Crawler as ScrapyCrawler
from scrapy.settings import Settings
from scrapy.xlib.pydispatch import dispatcher
from scrapy.utils.project import get_project_settings

def scrapy_crawl(name):

    def stop_reactor():
        reactor.stop()

    dispatcher.connect(stop_reactor, signal=signals.spider_closed)
    scrapy_settings = get_project_settings()
    crawler = ScrapyCrawler(scrapy_settings)
    crawler.configure()
    spider = crawler.spiders.create(name)
    crawler.crawl(spider)
    crawler.start()
    log.start()
    reactor.run()


if __name__=='__main__':
    scrapy_crawl("kuchuan_totaldown_spider")
