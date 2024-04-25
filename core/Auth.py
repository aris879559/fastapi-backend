# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月25日
@Env: python 3.8.10
@Desc: JWT鉴权
"""

from fastapi import Request
from fastapi.security import SecurityScopes


async def check_permissions(req: Request, security_scopes: SecurityScopes):
    """
    权限验证
    :param req:
    :param security_scopes:
    :return:
    """
    pass