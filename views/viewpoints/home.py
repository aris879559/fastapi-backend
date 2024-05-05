# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月03日
@Env: python 3.8.10
@Desc: home 视图
"""
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", tags=["门户首页"], response_class=HTMLResponse)
async def home(request: Request):
    """
    门户首页
    :param request:
    :return:
    """
    return request.app.state.views.TemplateResponse("index.html", {"request": request})