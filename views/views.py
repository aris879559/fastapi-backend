# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月03日
@Env: python 3.8.10
@Desc: 视图路由
"""
from fastapi import APIRouter
from views.viewpoints import home

views_router = APIRouter()
views_router.include_router(home.router)