# -*- coding: utf-8 -*-
import pymysql
from scrapy_test1.items import InfoItem
from scrapy_test1.utils.mylog import write2log
from scrapy_test1.pipelines import BasePipeline
from scrapy_test1.utils import db


class DownPipeline(BasePipeline):
    def process_item(self, item, spider):
        assert isinstance(item, InfoItem)
        results = item['results']
        if not results:
            write2log('pipline得到空result')
            return item

        if item['spider_name'] is 'kuchuan_totaldown_spider':
            sql_insert = 'insert into tb_records_detail(app_id,market,tick,downloads_total)  ' \
                         'values '
        elif item['spider_name'] is 'kuchuan_dailydown_spider':
            #!!! 表中time字段改成tick
            sql_insert = 'insert into tb_records_day(app_id,market,tick,downloads_total)  ' \
                         'values '
        else:
            return item

        pkgname = results['pkgname']
        app_id = db.get_appid(pkgname)
        tick = results['tick']
        data = results['data']
        values = []
        for market, down in data.items():
            values.append('("{0}", "{1}", "{2}", "{3}" )'.format(
                app_id, market, tick, down
            ))
        sql_insert += ','.join(values)

        res = db.myCreate(sql_insert)
        if res:
            write2log('tb_records_detail 插入成功')

        return item


if __name__ == '__main__':
    # conn=pymysql.connect('localhost','root','rrrrrr','analyse_data') # <pymysql.connections.Connection>
    # cursor=conn.cursor() # <pymysql.cursors.Cursor>
    with pymysql.connect('localhost', 'root', 'rrrrrr', 'analyse_data') as cursor:
        write2log('select version: ' + str(cursor.execute('select version()')))
        write2log('new down info add to mysql')
