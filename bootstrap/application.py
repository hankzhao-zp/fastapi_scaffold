# -*- encoding: utf-8 -*-
# @File    :   application.py
# @Time    :   2024/12/25 11:49:31
# @Author  :   HankZhao 
# @Desc    :   服务应用注册和启动相关


from app.core import fastapi_app, router_app

from fastapi import FastAPI
from loguru import logger


def create_app() -> FastAPI:
    logger.info("app initialize begin...")
    
    app = FastAPI()
    
    register(app=app, core_provider=fastapi_app)
    boot(app=app, core_provider=router_app)
    
    return app
    
    
def register(app, core_provider):
    logger.info(core_provider.name + " registering")
    core_provider.register(app)


def boot(app: FastAPI, core_provider):
    logger.info(core_provider.name + " booting")
    core_provider.boot(app)
