# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本配置文件
"""

import os.path
from pydantic_settings  import BaseSettings
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "https://localhost:3003",
# ]

class Config(BaseSettings):
  # 加载数据库环境变量，有就会覆盖
  load_dotenv(find_dotenv(), override=True)
  # 调试模式
  APP_DEBUG: bool = True
  # 项目信息
  VERSION: str = "0.0.1"
  PROJECT_NAME: str = "fastapi"
  DESCRIPTION: str = '<a href="/redoc" target="_blank">redoc</a>'
  # 静态资源目录
  STATIC_DIR: str = os.path.join(os.getcwd(), "static")
  TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
  # 跨域请求
  # CORS_ORIGINS: List[str] = ['*']
  CORS_ORIGINS: List[str] = ['http://localhost:3003']
  # CORS_ORIGINS: List[str] = origins
  CORS_ALLOW_CREDENTIALS: bool = True
  CORS_ALLOW_METHODS: List[str] = ['*']
  CORS_ALLOW_HEADERS: List[str] = ['*']

  #session 缓存配置，配置session过期时间为14天
  SECRET_KEY: str = "session"
  SESSION_COOKIE: str = "session_id"
  SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
  # SESSION_MAX_AGE: int = 6

  # jwt
  JWT_SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
  JWT_ALGORITHM: str = "HS256"
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 60

  SWAGGER_UI_OAUTH2_REDIRECT_URL: Optional[str] = "/v1/test/oath2"

settings = Config()