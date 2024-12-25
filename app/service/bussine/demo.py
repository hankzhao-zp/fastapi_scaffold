# -*- encoding: utf-8 -*-
# @File    :   demo.py
# @Time    :   2024/12/25 11:15:14
# @Author  :   HankZhao 
# @Desc    :   


from app.schemas.base.response import Response
from app.util.make_response import fail_response, success_response

from loguru import logger


class Demo:
    
    def __init__(self):
        pass
    
    
    @logger.catch
    def demo(self):
        logger.info("demo")
        return success_response(data="demo")


    @logger.catch
    def demo_fail(self):
        logger.info("demo_fail")
        return fail_response(data="demo_fail")
