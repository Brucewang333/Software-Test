import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://hmshop-test.itheima.net/Home/user/login.html")
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test01_login(self):
        # 输入用户名
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys('admin')
        # 输入密码
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys('123456')
        # 输入验证码
        self.driver.find_element(By.CSS_SELECTOR, "#verify_code").send_keys('8888')
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".submit").click()
