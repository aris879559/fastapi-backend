# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年05月03日
@Env: python 3.8.10
@Desc: 测试
"""
from core.Auth import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException

async def test_oath2(data: OAuth2PasswordRequestForm = Depends()):
  user_type = False
  if not data.scopes:
    raise HTTPException(401, "请选择作用域!")
  if "is_admin" in data.scopes:
    user_type = True
  jwt_data = {
    "user_id": data.client_id,
    "user_type": user_type
  }
  jwt_token = create_access_token(data=jwt_data)

  return {"access_token": jwt_token, "token_type": "bearer"}
