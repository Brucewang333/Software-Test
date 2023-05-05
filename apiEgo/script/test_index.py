import logging
import unittest

import app
from api.index import IndexApi


class TestIndex(unittest.TestCase):

    # 初始化类方法，已封装接口实例化一个对象
    @classmethod
    def setUp(cls) -> None:
        cls.index_api = IndexApi()

        # 调用已封装的测试接口
        # 调用获取轮播图接口的方法
        def test01_get_banner(self):
            # 测试数据
            banner_id = app.bid
            # 发送请求

            response = self.index_api.get_banner(banner_id)
            json_data = response.json()
            logging.info(f"获取轮播图的结果为：{json_data}")
            # 断言结果
            self.assertEqual(200, response.status_code)  # 断言响应状态码
            self.assertEqual(banner_id, json_data.get("id"))  # 断言响应数据id

        # 调用获取专题栏位的接口
        def test02_get_theme(self):
            # 测试数据
            ids = app.ids
            # 发送请求
            response = self.index_api.get_theme(ids)
            json_data = response.json()
            logging.info(f"获取专题栏位的结果:{json_data}")
            # 断言结果
            self.assertEqual(200, response.status_code)
            self.assertIsNotNone(len(json_data))  # 断言列表的长度大于0（列表不为空）

            # self.assertEqual(1, json_data[0].get("id"))  # 将列表元素取出来然后在断言

            # 调用获取最近新品接口
            def test03_get_recent_product(self):
                # 测试数据
                # 发送请求
                response = self.index_api.get_recent_product()
                json_data = response.json()
                logging.info(f"获取最近新品结果：{json_data}")
                # 结果断言
                self.assertEqual(200, response.status_code)
                self.assertIsNotNone(len(json_data))
