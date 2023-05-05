from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
# 设置中⽂
desired_caps["nicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

'''
appium中封装了⼿势的操作⽅法，都在TouchAction类中，需要导包
所有的⼿势操作，最终都需要调⽤perform()⽅法才能执⾏
    手势操作: TouchAction类
        1、轻敲：（元素，x，y）
    #需求：
        1、请求WLAN
'''
# 获取WLAN元素
wlan = driver.find_element(By.XPATH, "//*[@text='WLAN']")
TouchAction(driver).tap(wlan).perform()  # 执行手势必须调用perform()方法
