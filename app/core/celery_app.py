# -*- encoding: utf-8 -*-
# @File    :   celery_app.py
# @Time    :   2024/12/25 11:35:28
# @Author  :   HankZhao 
# @Desc    :   


from app.config import celery_config
from app.config.settings import settings

from celery import Celery


celery_app = Celery(main=celery_config.app_name, broker=settings.CELERY_BROKER_URL)
celery_app.config_from_object(celery_config)
celery_app.autodiscover_tasks(['app.worker'])
