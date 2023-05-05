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
       切换任意窗口
    
    如何切换？
        1、获取所有窗⼝句柄 driver.window_handles
        2、使⽤句柄切换遍历窗⼝ driver.switch_to.widnow(handle)
        3、获取当前窗口的title
        4、判断title是否为需要的窗口
        句柄：窗⼝的唯⼀标识符。
        
    需求：
        1、打开注册示例页面
        2、点击 注册A网页 注册B网页
        3、在A网页和B网页中输入 对用户名输入 admin
'''


def switch_window(title):
    # 获取所有窗口句柄
    handles = driver.window_handles

    # 遍历句柄进行切换
    for handle in handles:
        # 操作
        driver.switch_to.frame(handle)
        # 获取当前窗口的title 判断是否为需要的窗口
        if driver.title == title:
            # 操作
            return "已找到{}窗⼝，并且已切换成功".format(title)


title_A = "注册A"
title_B = "注册B"

# 打开注册A和注册B⽹⻚
driver.find_element(By.LINK_TEXT, "注册A⽹⻚").click()
driver.find_element(By.LINK_TEXT, "注册B⽹⻚").click()

# 填写注册A⽹⻚ ⽤户名
switch_window(title_A)
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")
# 填写注册B⽹⻚ ⽤户名
switch_window(title_B)
driver.find_element(By.CSS_SELECTOR, "#userB").send_keys("admin")

# 关闭浏览器
sleep(3)
driver.quit()
