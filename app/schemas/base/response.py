# -*- encoding: utf-8 -*-
# @File    :   response.py
# @Time    :   2024/12/25 10:47:12
# @Author  :   HankZhao 
# @Desc    :   response数据结构


from pydantic import BaseModel


class Response(BaseModel):
    success: bool = False
    message: str
    data: object
