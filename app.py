# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
app运行时文件
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from core.Router import AllRouter
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException, \
    mysql_operational_error, mysql_does_not_exist
from core.Middleware import Middleware
from fastapi.templating import  Jinja2Templates
from tortoise.exceptions import OperationalError, DoesNotExist
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html)
from core import Router

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME,
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=settings.SWAGGER_UI_OAUTH2_REDIRECT_URL,
    )

# custom_openapi
def custom_openapi():
    if application.openapi_schema:
        return application.openapi_schema
    openapi_schema = get_openapi(
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        title=settings.PROJECT_NAME,
        routes=app.routes,
    )
    openapi_schema["openapi"] = "3.0.0"
    openapi_schema["info"]["version"] = settings.VERSION
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/logo-teal.png"
    }
    application.openapi_schema = openapi_schema
    return application.openapi_schema


application.openapi = custom_openapi


# custom_swagger_ui_html
@application.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=application.openapi_url,
        title=application.title + " - Swagger UI",
        oauth2_redirect_url=application.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


# swagger_ui_oauth2_redirect_url
# @application.get(application.swagger_ui_oauth2_redirect_url, include_in_schema=False)
# async def swagger_ui_redirect():
#     return get_swagger_ui_oauth2_redirect_html()


# redoc
@application.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=application.openapi_url,
        title=application.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )

# 事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))


# 异常错误处理
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)
application.add_exception_handler(DoesNotExist, mysql_does_not_exist)
application.add_exception_handler(OperationalError, mysql_operational_error)

# 路由
application.include_router(AllRouter)

# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 静态资源目录
application.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")))
application.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)
app = application
