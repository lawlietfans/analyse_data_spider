#!/usr/bin/env python
# encoding: utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
__author__ = 'fengshenjie'

# yingyongbao_appinfo_spider

# -*- coding: utf-8 -*-
import pymysql
from scrapy_test1.items import InfoItem
from scrapy_test1.utils.mylog import write2log
from scrapy_test1.utils import db


class BasePipeline():
    def __init__(self, db_url, db_user, db_pwd, db_name):
        self.db_url = db_url
        self.db_user = db_user
        self.db_pwd = db_pwd
        self.db_name = db_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(db_url=crawler.settings.get('DB_URL'),
                   db_user=crawler.settings.get('DB_USER'),
                   db_pwd=crawler.settings.get('DB_PWD'),
                   db_name=crawler.settings.get('DB_NAME'))

    # def open_spider(self, spider):
    #     self.db=pymysql.connect(self.db_url, self.db_user, self.db_pwd, self.db_name)
    #
    # def close_spider(self, spider):
    #     self.db.close()

    def process_item(self, item, spider):
        raise NotImplementedError


class AppinfoPipeline(BasePipeline):
    def process_item(self, item, spider):
        assert isinstance(item, InfoItem)
        if item['spider_name'] != 'yingyongbao_appinfo_spider':
            return item

        from scrapy_test1.utils.db import myRetrieve, myCreate, myUpdate
        results = item['results']
        sql_ishas = 'select id from tb_apps where package="{}"'.format(
            results['package']
        )
        data = myRetrieve(sql_ishas)
        if data:
            sql_update = 'update tb_apps ' \
                         'set name="{name}", ' \
                         'developer="{developer}", ' \
                         'description="{description}" ' \
                         'where package="{package}"'.format(**results)
            res = myUpdate(sql_update)
            if res:
                write2log('tb_apps 更新成功')
        else:
            sql_insert = "insert into tb_apps(name,developer,description,package) " \
                         "values('{0}', '{1}', '{2}', '{3}')".format(
                results['name'], results['developer'], results['description'], results['package']
            )
            if myCreate(sql_insert):
                write2log('tb_apps插入成功')

        return item


class VersionPipeline(BasePipeline):
    def process_item(self, item, spider):
        assert isinstance(item, InfoItem)
        if item['spider_name'] != 'kuchuan_version_spider':
            return item
        results = item['results']
        pkgname = results['packagename']
        appid = db.get_appid(pkgname)
        data = results['data']
        latest_version = data[0]['versionname']
        sql_maxversion = 'select max(name) from tb_version_history'
        res = db.myRetrieve(sql_maxversion)
        res = res[0][0]
        if res == latest_version:
            return item

        sql_add = 'insert into ' \
                  'tb_version_history(app_id, name, update_time, update_description) ' \
                  'values '
        values = []
        if res:
            for d in data:
                if d['versionname'] <= latest_version:
                    break
                values.append('("{0}", "{1}", "{2}", "{3}")'.format(
                    appid, d['versionname'], d['begintime'], d['updatecontent']
                ))
        else:
            for d in data:
                values.append('("{0}", "{1}", "{2}", "{3}")'.format(
                    appid, d['versionname'], d['begintime'], d['updatecontent']
                ))
        sql_add += ','.join(values)
        res = db.myCreate(sql_add)
        if res:
            write2log('tb_version_history插入成功')
        return item


class ScorePipeline(BasePipeline):
    def process_item(self, item, spider):
        assert isinstance(item, InfoItem)
        if item['spider_name'] != 'yingyongbao_score_spider':
            return item

        results = item['results']
        pkgname = results['pkgname']
        appid = db.get_appid(pkgname)
        if appid < 0:
            return item
        results['app_id']=appid
        sql_insert = 'insert into tb_score_sum(app_id, market, date, score) ' \
                     'values ("{app_id}", "{market}", "{date}", "{score}")'.format(
            **results
        )
        res = db.myCreate(sql_insert)
        if res:
            write2log('tb_score 插入成功')
        return item


if __name__ == '__main__':
    pass
