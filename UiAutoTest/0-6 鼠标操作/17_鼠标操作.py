from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 实例化鼠标对象
action = ActionChains(driver)

# 练习1 查找注册按钮
el = driver.find_element(By.CSS_SELECTOR, "button")

# 鼠标悬停
action.move_to_element(el).perform()
sleep(2)

# 练习2
username = driver.find_element(By.CSS_SELECTOR, "userA")
# 鼠标右击
action.context_click(username).perform()
sleep(2)

# 练习3
username.send_keys("admin")
sleep(3)
# 鼠标双击
action.double_click(username).perform()

# 练习4
# 鼠标拖拽

div1 = driver.find_element(By.CSS_SELECTOR, "#div1")
div2 = driver.find_element(By.CSS_SELECTOR, "#div2")
action.drag_and_drop(div1, div2).perform()

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
