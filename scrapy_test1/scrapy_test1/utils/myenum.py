# encoding: utf-8
__author__ = 'fengshenjie'

# from enum import Enum,IntEnum,unique #  http://www.cnblogs.com/sanghai/p/6243529.html


def enum(**enums):
    return type('Enum', (), enums)
