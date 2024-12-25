# -*- encoding: utf-8 -*-
# @File    :   demo_helper.py
# @Time    :   2024/12/25 11:56:59
# @Author  :   HankZhao 
# @Desc    :   


from loguru import logger


class DemoHelper:
    
    def __init__(self):
        pass
    
    @logger.catch
    def demo(self):
        logger.info("demo helper")
