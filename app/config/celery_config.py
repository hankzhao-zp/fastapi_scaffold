# -*- encoding: utf-8 -*-
# @File    :   celery_config.py
# @Time    :   2024/12/25 11:36:38
# @Author  :   HankZhao 
# @Desc    :   celery配置


from app.config.settings import settings

from kombu import Queue
from celery.schedules import crontab


# celery 基础配置
app_name: str = "worker_app_name"
task_serializer: str = "json"
result_serializer: str = "json"
accept_content: list = ['json']
timezone: str = settings.TIMEZONE
enable_utc: bool = False
result_expires : int = 60 * 60 * 24
broker_connection_retry_on_startup: bool = True


# 默认队列名
DEFAULT_QUEUE_NAME: str = "default_worker_task_queue"
DEFAULT_ROUTE_KEY: str = "default_worker"


# 特殊任务相关的任务名, 队列名和路由值
SPECIAL_TASK_NAME: str = "app.worker.special_worker.run"
SPECIAL_TASK_QUEUE_NAME: str = "sepcial_worker_task_queue_name"
SPECIAL_TASK_ROUTE_KEY: str = "special_worker_task_route_key"


task_queues = (
    Queue(name=DEFAULT_QUEUE_NAME, routing_key=DEFAULT_ROUTE_KEY),
    Queue(name=SPECIAL_TASK_QUEUE_NAME, routing_key=SPECIAL_TASK_ROUTE_KEY)
)

task_routes = { 
    SPECIAL_TASK_NAME: {
        'queue': SPECIAL_TASK_QUEUE_NAME, 
        'routing_key': SPECIAL_TASK_ROUTE_KEY 
    }
}

beat_schedule = {
    SPECIAL_TASK_ROUTE_KEY: {
        'task': SPECIAL_TASK_NAME,
        # 'schedule': crontab(hour=2, minute=0, day_of_week='sunday'),
        'schedule': crontab(minute='*/1'),
        'args': (),
    }
}
