# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
视图路由
"""
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates
from config import settings
from views.home import home, req_page, result_page, session_test


ViewsRouter = APIRouter()

# templates = Jinja2Templates(directory=settings.templates_path)
# templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)

# # 方式一
# @ViewsRouter.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     # return templates.TemplateResponse("index.html", {"request": request, "id": id})
#     return templates.get_template("index.html").render({"request": request, "id": id})

# 方式二
# ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)

ViewsRouter.get("/req", response_class=HTMLResponse)(req_page)
ViewsRouter.post("/req/form", response_class=HTMLResponse)(result_page)

ViewsRouter.get("/session_test", response_class=HTMLResponse)(session_test)

ViewsRouter.get("/", tags=["门户首页"], response_class=HTMLResponse)(home)