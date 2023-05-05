import unittest
from parameterized import parameterized
import page
from page.page_app_login import PageAppLogin
from page.page_app_order import PageAppOrder
from util import GetDriver, read_json


class TestAppLoginOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver.get_app_driver()
        # 获取PageAppLogin的实例
        self.app = PageAppLogin(self.driver)
        # 获取PageAppOrder的实例对象
        self.order = PageAppOrder(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand(read_json("app_order.json", 'order'))
    def test01_login_order(self, text_value, pwd, expect_nickname):
        try:
            # 调用登录
            self.app.page_app_login()
            # 打印昵称 -> 断言
            nickname = self.app.page_app_get_nickname()
            print("登录账户的昵称为:", nickname)
            self.assertEqual(expect_nickname, nickname)
            # 下订单
            self.order.page_app_order(text_value, pwd)

            # 获取订单编号 -> 断言
            order_no = self.order.page_app_get_order_no()

            print('订单的编号:', order_no)
            # 记录订单编号 --> 发货完成后做断言使用
            page.order_no = order_no
        except Exception as e:
            print("错误原因：", e)
            raise
