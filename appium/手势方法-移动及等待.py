from time import sleep

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
        1、轻敲：(元素，x，y)
        2、按下：press(el,x,y)
        3、释放：release()
        4、⻓按：long_press(el,x,y)
        5、移动：move_to(el,x,y)
        6、等待： wait()
    #需求：
        绘制解锁图案
'''

# 1、定位WLAN
wlan = driver.find_element(By.XPATH, "//*[@text='WLAN']")
# 2、定位应用
app = driver.find_element(By.XPATH, "//*[@text='应用']")

# 拖拽页面到 安全 出现
driver.drag_and_drop(app, wlan)
# 3、点击安全
driver.find_element(By.XPATH, "//*[@text='安全']").click()
# 4、点击屏幕锁定方式
driver.find_element(By.XPATH, "//*[@text='屏幕锁定方式']").click()
# 5、点击图案
driver.find_element(By.XPATH, "//*[@text='图案']").click()
# 必须暂停，登录绘制⻚⾯加载完成
sleep(2)
# 6、绘制
TouchAction(driver).press(x=1048, y=340).wait(100).move_to(x=1377, y=340). \
    wait(100).move_to(x=1707, y=340).wait(100).move_to(x=1377, y=669).wait(100). \
    move_to(x=1048, y=999).wait(100).move_to(x=1377, y=999).wait(100). \
    move_to(x=1707, y=999).wait(100).perform()

sleep(3)
driver.quit()
