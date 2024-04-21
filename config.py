# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本配置文件
"""

import os.path
from pydantic_settings  import BaseSettings
from typing import List


class Config(BaseSettings):
  # 调试模式
  APP_DEBUG: bool = True
  # 项目信息
  VERSION: str = "0.0.1"
  PROJECT_NAME: str = "fastapi-demo"
  DESCRIPTION: str = 'fastapi项目demo'
  # 静态资源目录
  STATIC_DIR: str = os.path.join(os.getcwd(), "static")
  TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
  # 跨域请求
  CORS_ORIGINS: List[str] = ['*']
  CORS_ALLOW_CREDENTIALS: bool = True
  CORS_ALLOW_METHODS: List[str] = ['*']
  CORS_ALLOW_HEADERS: List[str] = ['*']


settings = Config()