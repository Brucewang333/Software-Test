from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 全局生效,所有元素第一次未找到触发 等待10秒
driver.implicitly_wait(10)
# 验证隐式等待
driver.find_element(By.CSS_SELECTOR, "#userA")

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
