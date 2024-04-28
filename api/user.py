# -*- coding: utf-8 -*-
"""
@Author: wei
@Date: 2024年04月25日
@Env: python 3.8.10
@Desc: 用户管理
"""
from core.Response import success, fail
from models.user import CreateUser,AccountLogin, UserInfo
from models.base import User, Role, Access
from core.Utils import en_password, check_password
from core.Auth import create_access_token
from fastapi.responses import JSONResponse
from fastapi import Request

async def user_info(req: Request):
    """
    获取当前登陆用户信息
    :param user_id: int
    :return:
    """
    user_data = await User.get_or_none(pk=req.state.user_id)
    if not user_data:
        return fail(msg=f"用户ID{req.state.user_id}不存在!")
    return success(msg="用户信息", data=UserInfo(**user_data.__dict__))


async def user_add(post: CreateUser):
    """
    创建用户
    :param post: CreateUser
    :return:
    """
    post.password = en_password(post.password)
    create_user = await User.create(**post.dict())
    if not create_user:
        return fail(msg=f"用户{post.username}创建失败!")
    return success(msg=f"用户{create_user.username}创建成功")


async def user_del(user_id: int):
    """
    删除用户
    :param user_id: int
    :return:
    """
    delete_user = await User.filter(pk=user_id).delete()
    if not delete_user:
        return fail(msg=f"用户{user_id}删除失败!")
    return success(msg="删除成功")


async def get_user_rules(user_id: int):
    """
    获取用户权限集合
    :param user_id:
    :return:
    """

    # 查询当前用户拥有的角色
    user_role = await Role.filter(user__id=user_id).values("role_name")
    # 查询当前用户的所有权限
    user_access_list = await Access.filter(role__user__id=user_id, is_check=True).values("id", "scopes")
    # 验证当前用户对当前域是否有权限
    is_pass = await Access.get_or_none(role__user__id=user_id, is_check=True, scopes="article_push", role__role_status=True)
    data = {
        "user_role": user_role,
        "pass": True if is_pass else False,
        "user_access_list": user_access_list
    }
    return success(msg="用户权限", data=data)

async def account_login(post: AccountLogin):
    """
    用户登录
    :param post: AccountLogin
    :return: jwt token
    """
    get_user = await User.get_or_none(username=post.username)
    if not get_user:
        return fail(msg=f"用户{post.username}密码验证失败！")
    if not check_password(post.password, get_user.password):
        return fail(msg=f"用户{post.username}密码验证失败！")
    if not get_user.user_status:
        return fail(msg=f"用户{post.username}已被管理员禁用禁用！")
    jwt_data = {
        "user_id": get_user.pk,
        "user_type": get_user.user_type
    }
    # 登录成功后生成token
    jwt_token = create_access_token(data=jwt_data)
    return success(msg="登录成功", data={"token": jwt_token})
    # return JSONResponse({
    #     "code": 200,
    #     "msg": "登录成功",
    #     "data": {}
    # }, status_code=200, headers={"Set-Cookie": "X-token=Bearer " + jwt_token})
