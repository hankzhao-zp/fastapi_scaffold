# -*- encoding: utf-8 -*-
# @File    :   special_worker.py
# @Time    :   2024/12/25 11:55:12
# @Author  :   HankZhao 
# @Desc    :   worker特殊任务


from app.core.celery_app import celery_app
from app.service.helper.demo_helper import DemoHelper
from app.config import settings

from loguru import logger

import os
import datetime


@celery_app.task()
def run():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(settings.BASE_PATH, 'storage', "logs", "worker", "special", f'{current_date}.log')
    logger.add(log_file_path, rotation="7 days", retention="7 days")
    
    logger.info("special worker run")
    demo_helper = DemoHelper()
    demo_helper.demo()
