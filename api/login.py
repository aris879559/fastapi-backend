# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
登录接口
"""
from typing import List
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str
    # user: List[int]


def register(age: int = 80):
    return {"fun": "/register", "age": age}

def login(data: Login):
    return data