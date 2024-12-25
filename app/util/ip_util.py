# -*- encoding: utf-8 -*-
# @File    :   ip_util.py
# @Time    :   2024/12/25 10:44:29
# @Author  :   HankZhao 
# @Desc    :   ip相关工具


import socket


def get_host_ip() -> str:
    try:
        ip = 'host_ip'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
