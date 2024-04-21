# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
views home
"""
from fastapi import Request


async def home(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
