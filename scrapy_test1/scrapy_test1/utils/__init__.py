#!/usr/bin/env python
# encoding: utf-8
__author__ = 'fengshenjie'
from scrapy.utils.project import get_project_settings
settings=get_project_settings()
import re
from scrapy_test1.utils.mylog import write2log


def get_pkg_list():
    return get_config_list('app_pkg_name.txt')

def get_config_list(filename):
    assert isinstance(filename, str)
    new_res = []
    with open(settings['MY_CONF_PATH']+filename, 'r', encoding='utf8') as fp:
        old_res = fp.readlines()
        for i in old_res:
            if i is '' or i is '\n' or i[0] is '#':
                pass
            else:
                new_res.append(i[:-1])
    return new_res

def findby_re(rule, txt):
    assert isinstance(rule,str)
    r=re.compile(rule)
    res=re.findall(r,txt)
    if res:
        return res[0]
    else:
        write2log('匹配失败'+rule+','+txt)
        return ''

marketmapper={
    '360': '360',
    'baidu': '百度',
    'yingyongbao': '应用宝',
    'wandoujia': '豌豆荚',
    'xiaomi': '小米',
    'huawei': '华为',
    'oppo': 'OPPO',
    'vivo': 'vivo',
    'meizu': '魅族',
    'lianxiang': '联想',
}


if __name__=='__main__':
    print(get_config_list('market.txt'))
    print(settings['DB_URL'])