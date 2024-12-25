# -*- encoding: utf-8 -*-
# @File    :   settings.py
# @Time    :   2024/12/25 10:43:41
# @Author  :   HankZhao 
# @Desc    :   配置文件


from app.util.ip_util import get_host_ip

import os


class Settings():
    NAME: str = "project name"
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    APP_ENV: str = 'test'
    DEBUG: bool = False
    HOST: str = get_host_ip()
    TIMEZONE: str = "Asia/Shanghai"
    
    # 服务相关地址和端口
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 7777
    
    
    # 服务log配置
    LOG_LEVEL: str = "DEBUG"
    LOG_PATH: str = os.path.join(BASE_PATH, "storage", "logs", "server", "{time:YYYY-MM-DD}.log")
    LOG_RETENTION: str = "7 days"
    
    # mysql 相关配置
    MYSQL_HOST: str = "mysql_host_address"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "user_name"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "database_name"
    MYSQL_ENGINE_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8"
    
    # rabbitmq相关
    RABBITMQ_HOST: str = "rabbitmq_host_address"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "user_name"
    RABBITMQ_PASSWD: str = "password"
    RABBITMQ_VHOST: str = "vhost"
    
    # celery相关
    CELERY_BROKER_URL: str = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}"

settings = Settings()
