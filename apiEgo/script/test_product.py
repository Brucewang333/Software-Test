# 导包
import unittest
import logging
from api.product import ProductApi


# 测试获取商品接口
class TestProduct(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        cls.product_api = ProductApi()

    # 测试获取商品分类
    def test01_get_all_category(self):
        # 发送请求
        response = self.product_api.get_all_category()
        json_data = response.json()
        logging.info(f"获取商品分类:{json_data}")
        # 断言结果
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json_data) > 0)

    # 测试获取商品下商品
    def test02_get_product_items(self):
        # 测试数据
        pid = 2
        # 发送请求
        response = self.product_api.get_product_items(pid)
        json_data = response.json()
        logging.info(f"商品分类下的商品:{json_data}")
        # 断言结果
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json_data))

    # 测试获取商品信息
    def test03_get_product_info(self):
        # 测试数据
        ids = 2
        # 发送请求
        response = self.product_api.get_product_info(ids)
        json_data = response.json()
        logging.info(f"获取商品信息:{json_data}")
        # 断言结果
        self.assertEqual(200, response.status_code)
        self.assertEqual(ids, json_data.get("id"))
