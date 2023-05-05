# 1.导包
import logging
import unittest

import app
from api.order import OrderApi


# 2.定义测试类
class TestOrder(unittest.TestCase):
    # 定义初始化方法：类方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.order_api = OrderApi()

    # 定义调用测试接口方法
    # 测试获取订单列表
    def test01_get_order_list(self):
        # 测试数据
        page = app.page
        # 发送请求
        response = self.order_api.get_order_list(page)
        json_data = response.json()
        logging.info(f"获取订单列表结果：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(page, json_data.get("current_page"))

    # 测试创建订单接口
    def test02_create_order(self):
        # 测试数据
        pid = app.product_id  # 商品编号
        count = app.count  # 商品数量
        # 发送请求
        response = self.order_api.creat_order(pid, count)
        json_data = response.json()
        logging.info(f"创建订单结果：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertTrue(json_data.get("pass"))
        # 创建后的订单保存到app中
        app.order_id = json_data.get("order_id")
        logging.info(f"保存的订单信息为：{app.order_id}")

    # 测试查看订单详情接口
    def test03_show_order(self):
        # 测试数据
        oid = int(app.order_id)  # 获取到的是字符串，需要转化为数字类型
        # 发送请求
        response = self.order_api.show_order(oid)
        json_data = response.json()
        logging.info(f"查看订单详情结果为：{json_data}")
        # 结果断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(oid, json_data.get("id"))
