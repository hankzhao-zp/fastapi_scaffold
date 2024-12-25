# -*- encoding: utf-8 -*-
# @File    :   database_app.py
# @Time    :   2024/12/25 11:32:55
# @Author  :   HankZhao 
# @Desc    :   数据库相关功能配置


from app.config import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database_engine = create_engine(settings.MYSQL_ENGINE_URL, echo=settings.DEBUG, pool_recycle=60, pool_pre_ping=True)

ApkSessionLocal = sessionmaker(bind=database_engine)
