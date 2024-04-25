# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本路由
"""
from fastapi import APIRouter, Request, Security
from api.login import register, login
from api.test_redis import test_redis, test_redis_depends

from core.Auth import check_permissions
from api.user import user_info, user_add, user_del, get_user_rules

#  创建一个路由器,设置ApiRouter的路由前缀/v1，所以调用ApiRouter的路由必须添加/v1，并设置标签为home
# 定义接口组home,
ApiRouter = APIRouter(prefix='/v1', tags=['Api路由'])


@ApiRouter.get('/',summary='首页接口')
# async def home(req: Request):
async def home(num: int):

    # return "fastapi is running"
    return {"num": num, "data": [{"num": num, "data": []},{"num": num, "data": []}]}

ApiRouter.get('/register',tags=['Api路由'],summary='注册接口')(register)
ApiRouter.post('/login',tags=['Api路由'],summary='登录接口')(login)

ApiRouter.get('/test/redis',tags=['Api路由'],summary='fastapi的state方式')(test_redis)
ApiRouter.post('/test/redis/depends',tags=['Api路由'],summary='fastapi依赖注入方式')(test_redis_depends)


ApiRouter.get("/admin/user/info",
              tags=["用户管理"],
              summary="获取用户信息",
              dependencies=[Security(check_permissions, scopes=["user_info"])]
              )(user_info)

ApiRouter.delete("/admin/user/del",
                 tags=["用户管理"],
                 summary="用户删除",
                 dependencies=[Security(check_permissions, scopes=["user_delete"])]
                 )(user_del)

ApiRouter.post("/admin/user/add",
               tags=["用户管理"],
               summary="用户添加",
               # dependencies=[Security(check_permissions, scopes=["user_add"])]
               )(user_add)

ApiRouter.get("/admin/user/rules",
              tags=["用户管理"],
              summary="查询用户权限",
              # dependencies=[Security(check_permissions, scopes=["user_add"])]
              )(get_user_rules)
