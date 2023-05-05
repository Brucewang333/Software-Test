from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 设置窗口大小
driver.set_window_size(100, 100)
sleep(2)

# js -> 向下
# js_down = "windows.scrollTo(0,10000)"
js_down = "windows.scrollTo(0,document.body.scrollHeight)"  # 动态获取页面高度
# 执行js方法
driver.execute_script(js_down)
sleep(2)

# js -> 向上
js_top = "windows.scrollTo(0,0)"
driver.execute_script(js_top)

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
