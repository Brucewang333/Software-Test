from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 点击弹窗
driver.find_element(By.CSS_SELECTOR, "#alertA").click()
sleep(2)

# 获取弹窗对象
el = driver.switch_to.alert

# 处理弹窗 同意/取消
# el.dismiss()
# sleep(2)

el.accept()
sleep(2)

# 输入用户名
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
