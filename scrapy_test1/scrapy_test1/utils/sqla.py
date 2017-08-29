# coding=utf-8
from sqlalchemy import create_engine,orm
from sqlalchemy.ext.declarative import declarative_base
from ..settings import CONN_STR,SQLECHO

engine = create_engine(CONN_STR,
                       max_overflow=5, encoding='utf-8', echo=SQLECHO,
                       pool_recycle=60 # 重连周期
                       )
modelbase = declarative_base()

Session= orm.sessionmaker(bind=engine)
# sess=Session()
