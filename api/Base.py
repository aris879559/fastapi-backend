# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本路由
"""
# from fastapi import APIRouter, Security
#
# from core.Auth import check_permissions
# from api.endpoint.user import user_info, user_add, user_del, account_login, test_oath2, user_list
#
# #  创建一个路由器,设置ApiRouter的路由前缀/v1，所以调用ApiRouter的路由必须添加/v1，并设置标签为home
# # 定义接口组home,
# ApiRouter = APIRouter(prefix='/v1')
# AdminRouter = APIRouter(prefix='/admin')
#
# # @ApiRouter.get('/',summary='首页接口')
# # # async def home(req: Request):
# # async def home(num: int):
# #
# #     # return "fastapi is running"
# #     return {"num": num, "data": [{"num": num, "data": []},{"num": num, "data": []}]}
# #
# # ApiRouter.get('/register',tags=['Api路由'],summary='注册接口')(register)
# # ApiRouter.post('/login',tags=['Api路由'],summary='登录接口')(login)
# # ApiRouter.get('/test/redis',tags=['Api路由'],summary='fastapi的state方式')(test_redis)
# # ApiRouter.post('/test/redis/depends',tags=['Api路由'],summary='fastapi依赖注入方式')(test_redis_depends)
# # ApiRouter.post("/user/account/login",tags=["用户管理"],summary="用户登录")(account_login)
#
# ApiRouter.post('/test/oath2',tags=["测试oath2授权"])(test_oath2)
#
# # AdminRouter.post("/account/login", response_model=UserLogin, tags=["管理员登录"],summary="用户登录")(account_login)
# AdminRouter.post("/account/login", tags=["管理员登录"],summary="用户登录")(account_login)
# AdminRouter.get("/user/info",
#               tags=["用户管理"],
#               summary="获取当前管理员信息",
#               dependencies=[Security(check_permissions, scopes=["user_info"])],
#               # response_model=CurrentUser
#               )(user_info)
#
# AdminRouter.get("/user/list",
#               tags=["用户管理"],
#               summary="获取管理员列表",
#               dependencies=[Security(check_permissions, scopes=["user_list"])],
#               # response_model=CurrentUser
#               )(user_list)
#
# AdminRouter.delete("/user/del",
#               tags=["用户管理"],
#               summary="管理员删除",
#               dependencies=[Security(check_permissions, scopes=["user_delete"])]
#               )(user_del)
#
# ApiRouter.post("/user/add",
#               tags=["用户管理"],
#               summary="管理员添加",
#               dependencies=[Security(check_permissions, scopes=["user_add"])]
#               )(user_add)
#
# # ApiRouter.get("/admin/user/rules",
# #               tags=["用户管理"],
# #               summary="查询用户权限",
# #               # dependencies=[Security(check_permissions, scopes=["user_add"])]
# #               )(get_user_rules)
# ApiRouter.include_router(AdminRouter)