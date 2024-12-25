# -*- encoding: utf-8 -*-
# @File    :   router_app.py
# @Time    :   2024/12/25 10:58:54
# @Author  :   HankZhao 
# @Desc    :   全局路由加载相关功能配置


from fastapi import FastAPI
from loguru import logger

from routes.api import api_router


def boot(app: FastAPI):
    app.include_router(api_router, prefix="/project_prefix")
    
    if app.debug:
        for router in app.routes:
            logger.debug('path : %s, name: %s, methods: %s' % (router.path, router.name, router.methods))

name = "app router"
