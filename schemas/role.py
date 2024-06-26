# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月03日
@Env: python 3.8.10
@Desc: 角色 schema
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.base import ResAntTable
from datetime import datetime


class CreateRole(BaseModel):
    role_name: str = Field(min_length=3, max_length=10)
    role_status: Optional[bool] = False
    role_desc: Optional[str] = Field(max_length=255)


class UpdateRole(BaseModel):
    id: int
    role_name: str
    role_status: Optional[bool]
    role_desc: Optional[str]


class RoleItem(BaseModel):
    id: int
    key: int
    role_name: str
    role_status: Optional[bool]
    role_desc: Optional[str]
    create_time: datetime
    update_time: datetime


class RoleList(ResAntTable):
    data: List[RoleItem]


class SetAccess(BaseModel):
    role_id: int
    access: List[int] = Field(default=[], description="权限集合")


class CreateAccess(BaseModel):
    access_name: str = Field("测试", description="权限名称")
    scopes: str = Field("test", description="权限标识")
    parent_id: int = 0
    is_check: bool = False
    is_menu: bool = False
