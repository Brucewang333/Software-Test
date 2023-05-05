# 导包
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取浏览器
driver = webdriver.Chrome()
# 打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")
# 隐式等待
driver.implicitly_wait(10)

# 查找操作元素
driver.find_element(By.CSS_SELECTOR, '#userA').send_keys('admin')
driver.find_element(By.CSS_SELECTOR, '#passwordA').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '#telA').send_keys('13656401994')
driver.find_element(By.CSS_SELECTOR, '#emailA').send_keys('admin@163.com')
'''
什么是截图？
    当前ui⻚⾯，截图保存。

为什么要截图？
    出错后，⽅便查看直观错误原因。
    
如何截图？
    driver.get_screenshot_as_file("xxx.png")
'''
# 截图
driver.get_screenshot_as_file("register.png")
driver.get_screenshot_as_file('error_{}.png'.format(time.strftime("%Y_%m_%D")))
# 关闭浏览器
sleep(3)
driver.quit()
