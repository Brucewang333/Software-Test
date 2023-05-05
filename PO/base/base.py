'''
base: 存放所有Page页面公共方法

'''
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=10, poll_frequency=0.5):
        # 显示等待可以查找元素
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(loc[0], loc[1]))
        pass

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入内容
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 获取文本值方法
    def base_get_text(self, loc):
        self.base_find(loc).text()
