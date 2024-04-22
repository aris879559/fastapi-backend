# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月22日
@Env: python 3.8.10
基础模型
"""
from tortoise import fields, Model
# from tortoise.models import Model


class User(Model):
  username = fields.CharField(null=True, max_length=20, description="用户名")
  user_type = fields.BooleanField(default=False, description="用户类型 True:超级管理员 False:普通管理员")
  password = fields.CharField(null=True, max_length=255)
  nickname = fields.CharField(default='wei', max_length=255, description='昵称')
  user_phone = fields.CharField(null=True, description="手机号", max_length=11)
  user_email = fields.CharField(null=True, description='邮箱', max_length=255)
  full_name = fields.CharField(null=True, description='姓名', max_length=255)
  user_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
  header_img = fields.CharField(null=True, max_length=255, description='头像')
  sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
  remarks = fields.CharField(null=True, max_length=30, description="备注")
  client_host = fields.CharField(null=True, max_length=19, description="访问IP")
  create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
  update_time = fields.DatetimeField(auto_now=True, description="更新时间")

  class Meta:
    table_description = "用户表"
    table = "user"