import unittest

from selenium import webdriver

from page.page_login import PageLogin
from parameterized import parameterized

from util import read_json


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://hmshoptest.itheima.net/Home/user/login.html")
        # 创建对象
        self.login = PageLogin(self.driver)

        pass

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    @parameterized.expand(read_json("login.json", "login"))
    def test01_login(self, phone, password, code, expect_text):
        try:
            # 调用登录业务
            self.login.page_login(phone, password, code)
            # 断言
            nickname = self.login.page_get_nickname()
            print("nickname:", nickname)
            self.assertEqual(nickname, expect_text)
        except Exception as e:
            print("error", e)
