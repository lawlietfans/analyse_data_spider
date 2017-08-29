# encoding: utf-8
__author__ = 'fengshenjie'
import os, time
# from scrapy.conf import settings # deprecation warning has been removed
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

def write2log(txt):
    txt = str(txt)
    logpath = settings['MY_LOG_PATH']
    if not os.access(logpath, os.W_OK):
        os.mkdir(logpath)
    with open(logpath + 'analyse_data.log', 'a+', encoding='utf8') as fp:
        print('###log: ' + txt)
        fp.write(time.strftime('%D %H:%M:%S', time.localtime()) + ':\n')
        fp.write(txt)
        fp.write('\n')


def write2errlog(txt, fp):
    pass


if __name__ == '__main__':
    write2log('中文')
