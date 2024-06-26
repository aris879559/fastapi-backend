# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月03日
@Env: python 3.8.10
@Desc: api路由
"""
from fastapi import APIRouter
from api.endpoints.test import test_oath2
from api.endpoints import user, role, access, websocket

api_router = APIRouter(prefix="/api/v1")
api_router.post("/test/oath2", tags=["测试oath2授权"])(test_oath2)
api_router.include_router(user.router, prefix='/admin', tags=["用户管理"])
api_router.include_router(role.router, prefix='/admin', tags=["角色管理"])
api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
api_router.include_router(websocket.router, prefix='/ws', tags=["WebSocket"])