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
# 设置中⽂
desired_caps["nicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

'''
    需求：
        1、查看当前⽹络类型
        2、设置⽹络类型为⻜⾏模式
        3、获取当前屏幕分辨率
        4、截图保存
        5、点击三次音量+   24
        6、点击返回       4
        7、点击两次音量-   25
        8、打开通知栏，点击通知栏的信息
'''
# 1、查看当前⽹络类型
print("当前⽹络类型为：", driver.network_connection)
# 2、设置⽹络类型为⻜⾏模式
driver.set_network_connection(1)
print("设置之后的⽹络类型为：", driver.network_connection)
# 3、获取当前屏幕分辨率
print("当前屏幕分辨率为：", driver.get_window_size())
# 4、截图保存
driver.get_screenshot_as_file("./screen.png")
# 5、点击三次音量+   24
i = 0
while i < 3:
    driver.press_keycode(24)
    i += 1
sleep(2)
# 6、点击返回       4
driver.press_keycode(4)
sleep(2)
# 7、点击两次音量-   25
i = 0
while i < 2:
    driver.press_keycode(25)
    i += 1

# 8、打开通知栏，点击通知栏的信息
driver.open_notifications()
sleep(2)
# 查找信息并点击
driver.find_element(By.XPATH, "//*[@text='应用宝.apk]").click()
sleep(3)
driver.quit()