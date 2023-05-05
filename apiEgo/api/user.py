# 1、导包
import requests

import app


# 2、封装接口类
class UserApi(object):
    # 定义初始化方法(init)
    def __init__(self):
        self.token_url = app.URL + "/api/v1/token/user"
        self.verify_url = app.URL + "/api/v1/token/verify"
        self.address_url = app.URL + "/api/v1/address"

    # 定义接口方法
    # 获取token
    def get_token(self, code):
        data = {"code": code}
        return requests.post(self.token_url, headers=app.header, json=data)

    # 验证token
    def verify_token(self, token):
        data = {"token": token}
        return requests.post(self.verify_url, headers=app.header, json=data)

    # 获取地址信息
    def get_address(self):
        return requests.get(self.address_url, headers=app.header)