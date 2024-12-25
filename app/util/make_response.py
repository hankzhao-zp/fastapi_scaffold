# -*- encoding: utf-8 -*-
# @File    :   make_response.py
# @Time    :   2024/12/25 10:46:03
# @Author  :   HankZhao 
# @Desc    :   response工具


from app.schemas.base.response import Response


def base(success: bool, message: str, data:object) -> Response:
    return Response(success = success, message=message, data=data)


def success_response(data: object=None) -> Response:
    return base(success=True, message="操作成功", data=data)
    
    
def fail_response(data: object=None) -> Response:
    return base(success=False, message="操作失败", data=data)
