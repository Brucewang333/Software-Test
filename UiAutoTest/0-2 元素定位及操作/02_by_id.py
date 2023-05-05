from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取浏览器
driver = webdriver.Chrome()
# 获取URL
driver.get("file:///Users/lgy/Documents/fodder/web/%E6%B3%A8%E5%86%8CA.html")

# 查找操作元素
driver.find_element(By.ID, "userA").send_keys('admin')
driver.find_element(By.ID, "passwordA").send_keys('123456')

# 关闭浏览器
sleep(3)
driver.quit()
