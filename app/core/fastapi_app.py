# -*- encoding: utf-8 -*-
# @File    :   fastapi_app.py
# @Time    :   2024/12/25 10:36:20
# @Author  :   HankZhao 
# @Desc    :   fastapi相关功能配置


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.config import settings


def register(app: FastAPI):
    app.debug = settings.DEBUG
    app.title = settings.NAME
    app.logger = logger
    
    add_global_middleware(app=app)
    
    
def add_global_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=["*"], 
        allow_credentials=True, 
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
name = "fastapi app"
