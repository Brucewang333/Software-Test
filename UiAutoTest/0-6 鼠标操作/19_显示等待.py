from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 显示等待 -> 返回查找到的元素 
el = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, "#userA"))
el.send_keys('admin')

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
