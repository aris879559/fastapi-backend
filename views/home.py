# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
views home
"""
from fastapi import Request, Form, Cookie
from models.base import User
from typing import Optional

async def home(request: Request, id: str):
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})

async def req_page(req: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return req.app.state.views.TemplateResponse("req_page.html", {"request": req})

async def result_page(req: Request, username: str = Form(...), password: str = Form(...)):
    """
    注册结果页面
    :param password: str
    :param username: str
    :param req
    :return: html
    """

    add_user = await User().create(username=username, password=password)
    print("新增用户id", add_user.pk)
    print("新增用户", add_user.username)

    user_list = await User().all().values()
    # 打印查询的所有结果
    for user in user_list:
        print(f"用户: {user.get('username')}", user)

    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("用户不存在")
        return {"info": "没有查询到用户"}

    # return req.app.state.views.TemplateResponse("req_result.html", {"request": req, "username": username, "password": password})
    return req.app.state.views.TemplateResponse("req_result.html", {"request": req, "username": get_user.username, "password": get_user.password})

async def session_test(request: Request,session_id: Optional[str] = Cookie(None)):
    cookie = session_id
    session = request.session.get("session")
    page_data = {
        "cookie": cookie,
        "session": session
    }
    request.session.setdefault("666", "somedata")
    return request.app.state.views.TemplateResponse("session.html", {"request": request, **page_data})
