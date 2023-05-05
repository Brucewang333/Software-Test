import json
import logging.handlers
import os

import appium.webdriver

from config import DIR_PATH, HOST
from selenium import webdriver


class GetDriver:
    __app_driver = None
    __web_driver = None

    # 获取App Driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '6.0.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'
            # APP包名 com.tpshop.malls/.SPMainActivity
            desired_caps['appPackage'] = "com.tpshop.malls"
            # 启动名
            desired_caps['appActivity'] = ".SPMainActivity"
            # 设置中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.__app_driver

    # 获取Web Driver
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.get(HOST)
            cls.__web_driver.maximize_window()
        return cls.__web_driver


# 读取json工具
def read_json(filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for data in json.load(f).get(key):
            arrs.append(tuple(data.values())[1:])
        return arrs


# 日志封装
class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = DIR_PATH + os.sep + "log" + os.sep + "thshop_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8'
                                                           )
            # 获取格式器
            fmt = '"%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"'
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log


if __name__ == '__main__':
    read_json("app_order.json", "order")
    GetLog.get_log().info('日志测试')
