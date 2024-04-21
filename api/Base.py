# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本路由
"""
from fastapi import APIRouter, Request
from api.login import register, login

#  创建一个路由器,设置ApiRouter的路由前缀/v1，所以调用ApiRouter的路由必须添加/v1，并设置标签为home
# 定义接口组home,
ApiRouter = APIRouter(prefix='/v1', tags=['Api路由'])


@ApiRouter.get('/',summary='首页接口')
# async def home(req: Request):
async def home(num: int):

    # return "fastapi is running"
    return {"num": num, "data": [{"num": num, "data": []},{"num": num, "data": []}]}

ApiRouter.get('/register',tags=['Api路由'],summary='注册接口')(register)
ApiRouter.get('/login',tags=['Api路由'],summary='登录接口')(login)