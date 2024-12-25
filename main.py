# -*- encoding: utf-8 -*-
# @File    :   main.py
# @Time    :   2024/12/25 10:24:28
# @Author  :   HankZhao 
# @Desc    :   主入口


from bootstrap.application import create_app
from app.config import settings
from app.core import log_app

import uvicorn


log_app.init()
app = create_app()

if __name__ == '__main__':
    config = uvicorn.Config(app=app, host=settings.SERVER_HOST, port=settings.SERVER_PORT, access_log=True, reload=True)
    server = uvicorn.Server(config=config)
    server.run()
