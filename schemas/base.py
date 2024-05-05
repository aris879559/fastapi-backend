# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月01日
@Env: python 3.8.10
@Desc: 基础schemas
"""
from pydantic import BaseModel, Field
from  typing import List, Optional, Any

class BaseResp(BaseModel):
    code: int = Field(description="状态码")
    message: str = Field(description="信息")
    data: List = Field(description="数据")


class ResAntTable(BaseModel):
    success: bool = Field(description="状态码")
    data: List = Field(description="数据")
    total: int = Field(description="总条数")

class WebsocketMessage(BaseModel):
    action: Optional[str]
    user: Optional[int]
    data: Optional[Any]