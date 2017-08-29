# encoding: utf-8
import subprocess
import sys, time, traceback
import schedule
from subprocess import Popen
from scrapy import cmdline


def crawl_down_info():
    # how to start
    cmdline.execute('scrapy crawl down_info_spider'.split())  # 2
    # sys.argv = ['scrapy', 'crawl', 'down_info_spider']
    # cmdline.execute() # 1

    # subprocess.Popen('scrapy crawl down_info_spider') # os.system('cmd a1 a2')也可以


def crawl_app_info():
    subprocess.Popen('scrapy crawl app_info_spider')


def crawl_comment_info():
    subprocess.Popen('scrapy crawl comment_info_spider')


def yingyongbao_appinfo():
    # subprocess.run('scrapy crawl yingyongbao_appinfo_spider'.split())
    cmdline.execute('scrapy crawl yingyongbao_appinfo_spider'.split())

def yingyongbao_score():
    cmd='scrapy crawl yingyongbao_score_spider'.split()
    cmdline.execute(cmd)

def kuchuan_version():
    cmd = 'scrapy crawl kuchuan_version_spider'.split()
    # subprocess.run(cmd)
    cmdline.execute(cmd)

def kuchuan_totaldown():
    cmd='scrapy crawl kuchuan_totaldown_spider'.split()
    cmdline.execute(cmd)

def kuchuan_dailydown():
    cmd='scrapy crawl kuchuan_dailydown_spider'.split()
    cmdline.execute(cmd)

if __name__ == '__main__':
    kuchuan_totaldown()

    # schedule.every().day.at('10:00').do(crawl_down_info)
    # schedule.every(1).minutes.do(crawl_down_info)
    # while True:
    #     try:
    #         schedule.run_pending()
    #         time.sleep(1)
    #     except Exception as e:
    #         traceback.print_exc()
