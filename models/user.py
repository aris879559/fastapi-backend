# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月25日
@Env: python 3.8.10
@Desc: 用户验证模型
"""
from pydantic import Field, BaseModel
from typing import Optional, List

class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=8, max_length=12)
    user_type: bool = Field(default=False)

class AccountLogin(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(min_length=8, max_length=12)

class UserInfo(BaseModel):
    id: int
    username: str
    # age: Optional[int]
    age: int = Field(default=None)
    user_type: bool
    nickname: Optional[str]
    user_phone: Optional[str]
    user_email: Optional[str]
    full_name: Optional[str]
    user_status: bool
    header_img: Optional[str]
    sex: int
