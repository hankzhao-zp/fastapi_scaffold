# -*- encoding: utf-8 -*-
# @File    :   api.py
# @Time    :   2024/12/25 11:00:24
# @Author  :   HankZhao 
# @Desc    :   加载子功能路由


from app.api import demo

from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(router=demo.router, tags=["api分类标签"])