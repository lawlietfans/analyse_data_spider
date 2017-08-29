# encoding: utf-8
__author__ = 'fengshenjie'
import pymysql
import traceback
from scrapy_test1.utils.mylog import write2log
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


def get_appid(pkg_name):
    '''
    get appid via app pkg name, str->int
    :param pkg_name(str):
    :return: appid(int)
    '''
    assert isinstance(pkg_name, str)
    sql = "select id from tb_apps " \
          "where package='{0}'".format(pkg_name)
    data = myRetrieve(sql)
    if data:
        return int(data[0][0])
    else:
        write2log('找不到pkgname对应的id')
        return -1


def myCreate(sql):
    assert 'insert' in sql
    return myCUD(sql)

def myUpdate(sql):
    assert 'update' in sql
    return myCUD(sql)


def myRetrieve(sql):
    assert 'select' in sql
    with pymysql.connect(settings['DB_URL'], settings['DB_USER'], settings['DB_PWD'],
                         settings['DB_NAME'], charset='utf8') as cursor:
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
            write2log(e)
            results = ()
    return results


def myDelete(sql):
    assert  'delete' in sql
    return myCUD(sql)

def myCUD(sql):
    '''create update delete'''
    with pymysql.connect(settings['DB_URL'], settings['DB_USER'], settings['DB_PWD'],
                         settings['DB_NAME'], charset='utf8') as cursor:
        try:
            cursor.execute(sql)
            cursor.connection.commit()
            res=True
        except Exception as e:
            cursor.connection.rollback()
            write2log(e)
            res=False
    return res


if __name__ == '__main__':
    # sql="insert into tb_apps values(98,'aname99','fsj','no descreption','com.fsj.99')"
    # print(myCreate(sql))
    print(get_appid('com.fsj.99'))
