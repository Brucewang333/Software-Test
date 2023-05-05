from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

# 定义字典变量
desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
# 注意：版本号必须正确
desired_caps["platformVersion"] = "7.1.1"
# android不检测内容，但是不能为空
desired_caps["deviceName"] = "192.168.56.101:5555"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"

# 获取toast
desired_caps['automationName'] = 'Uiautomator2'

# 设置中⽂
desired_caps["nicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

'''
    获取toast消息
        说明： toast消息为移动应⽤中，⼀种⿊底⽩字提示信息，有时间限制。
    为什么要获取toast消息？
        断⾔内容
    如何获取？
        安装依赖库   pip install uiautomator2
        配置driver启⽤参数    desired_caps['automationName'] = 'Uiautomator2'
        编写代码获取⽂本值     
'''

# 获取网易新闻未同意协议进行登录 --> toast信息

driver.find_element(By.XPATH, '//*[@text="未登录"]').click()
driver.find_element(By.XPATH, '//*[@text="登录"]').click()
driver.find_element(By.XPATH, '//*[@text="微信登录"]').click()

msg = driver.find_element(By.XPATH, '//*[contains(@text,"请先勾选同意")]').text
print("toast消息为:", msg)
sleep(3)
driver.quit()