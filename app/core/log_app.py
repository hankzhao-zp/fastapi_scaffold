# -*- encoding: utf-8 -*-
# @File    :   log_app.py
# @Time    :   2024/12/25 10:56:03
# @Author  :   HankZhao 
# @Desc    :   日志相关功能配置


from loguru import logger

from app.config import settings

import logging
import sys


def init():
    logger.info("the service logging function loading....")
    level = settings.LOG_LEVEL
    path = settings.LOG_PATH
    retention = settings.LOG_RETENTION

    logging.getLogger().handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler]
    logger.configure(handlers=[
        {"sink": sys.stdout, "level": level},
        {"sink": path, "rotation": "00:00", "retention": retention, "level": level},
    ])
    
    logger.info("The service logging function is loaded")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

name = "log app"