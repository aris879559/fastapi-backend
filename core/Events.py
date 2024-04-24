# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
fastapi事件监听
"""
from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql

from database.redis import sys_cache, code_cache
from aioredis import Redis

def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP启动完成后触发
        print("启动完毕")
        #注册数据库
        await register_mysql(app)
        #注入缓存到app
        app.state.cache = await sys_cache()
        # app.state.code_cache = await code_cache()
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def stop_app() -> None:
        # APP停止时触发
        print("停止")

        cache: Redis = await app.state.cache
        # code: Redis = await app.state.code_cache
        await cache.close()
        # await code.close()
        pass

    return stop_app
