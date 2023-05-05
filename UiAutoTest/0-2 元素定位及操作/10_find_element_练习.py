# 1.导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.创建浏览器对象,打开浏览器
driver = webdriver.Chrome
driver.get("http://hmshop-test.itheima.net/")
# 3.查找操作元素
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "[name='passwordA']").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("16656006666")
driver.find_element(By.CSS_SELECTOR, "[palaceholder*='电子']").send_keys("Wang@163.com")
# 修改电话
sleep(3)
driver.find_element(By.CSS_SELECTOR, ".telA").clear()
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("16656008666")

# 点击注册
driver.find_element(By.CSS_SELECTOR, "button").click()

# 4.关闭浏览器
sleep(2)
driver.quit()
