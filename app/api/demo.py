# -*- encoding: utf-8 -*-
# @File    :   demo.py
# @Time    :   2024/12/25 11:08:16
# @Author  :   HankZhao 
# @Desc    :   


from app.schemas.base.response import Response
from app.service.bussine.demo import Demo

from fastapi import APIRouter
from loguru import logger


router = APIRouter()

@router.get(path="/demo", name='api功能名', response_model=Response)
@logger.catch
def demo():
    demo = Demo()
    return demo.demo()
