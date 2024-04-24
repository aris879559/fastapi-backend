# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月23日
@Env: python 3.8.10
@Desc: redis test
"""
from fastapi import Depends, Request
from database.redis import sys_cache
from aioredis import Redis
from core.Response import success

async def test_redis(req: Request):
  # 连接池放在request
  value = await req.app.state.cache.get("today")
  return success(msg="redis test success",data=[value])

async def test_redis_depends(today: int,cache: Redis = Depends(sys_cache)):
  # 连接池放在依赖注入,name等同于name，value即值，ex为过期时间s
  await cache.set(name="today", value=today, ex=60)
  value = await cache.get("today")
  return success(msg=f"今天是{today}号",data=[value])