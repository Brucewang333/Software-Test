# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取浏览器
driver = webdriver.Chrome()
# 打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")
# 隐式等待
driver.implicitly_wait(10)

'''
    为什么要处理多窗口？ --selenium默认启动时，所有的焦点在启动窗⼝，那么意味着⽆法操作其他窗⼝的标签。
    需求：
        1、打开注册示例页面
        2、点击注册A网页链接
        3、填写注册A网页内容
    
    如何切换？
        1、获取窗⼝句柄 driver.window_handles
        2、使⽤句柄切换窗⼝ driver.switch_to.widnow(handle)
        句柄：窗⼝的唯⼀标识符。
'''
print("操作之前所有窗⼝的句柄：", driver.window_handles)

driver.find_element(By.CSS_SELECTOR, "注册A网页").click()

handles = driver.window_handles
print("操作之后所有窗⼝的句柄：", handles)
# 重点：切换窗⼝
driver.switch_to.window(handles[1])

# 填写注册A网页 用户名
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys('admin')

# 关闭浏览器
sleep(3)
driver.quit()