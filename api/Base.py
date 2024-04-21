# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月21日
@Env: python 3.8.10
基本路由
"""
from fastapi import APIRouter, Request
router = APIRouter()


@router.get('/')
# async def home(req: Request):
async def home(num: int):

    # return "fastapi is running"
    return num
