# 1.导包
import logging
import unittest

import app
from api.user import UserApi


# 2.定义测试接口类
class TestUser(unittest.TestCase):

    # 定义初始化方法(类方法)
    @classmethod
    def setUp(self) -> None:
        self.user_api = UserApi()

    # 定义调用接口方法
    def test01_get_token(self):
        # 调用获取token接口
        # 测试数据
        code = code = app.CODE
        # 发送请求
        response = self.user_api.get_token(code)
        json_data = response.json()
        logging.info(f"获取token的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(32, len(json_data.get("token")))  # 断言token值的长度是否是32
        self.assertIn("token", json_data)  # 断言包含关键词token
        # 保存token值（app.py配置文件中）
        app.header["token"] = json_data.get("token")  # 字典名["键"] = 值
        logging.info(f"保存的token值：{app.header['token']}")

    # 调用验证token接口
    def test02_verify_token(self):
        # 测试数据
        token = app.header["token"]
        # 发送请求
        response = self.user_api.verify_token(token)
        json_data = response.json()
        logging.info(f"验证token的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, json_data.get("isValid"))
        self.assertTrue(json_data.get("isValid"))

    # 调用获取地址信息接口
    def test03_get_address(self):
        # 测试数据
        # 发送请求
        response = self.user_api.get_address()
        json_data = response.json()
        logging.info(f"获取地址信息结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(app.phone, json_data.get("mobile"))
        self.assertEqual(app.name, json_data.get("name"))