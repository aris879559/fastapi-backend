# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
路由聚合
"""
# from api.Base import ApiRouter
# from views.Base import ViewsRouter
# from fastapi import APIRouter

from api.api import api_router
from views.views import views_router
from fastapi import APIRouter

#  路由聚合，总路由配置
AllRouter = APIRouter()
# 视图路由
AllRouter.include_router(views_router)
# API路由
AllRouter.include_router(api_router)
