# 1.导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.创建浏览器对象,打开浏览器
driver = webdriver.Chrome
driver.get("http://hmshop-test.itheima.net/")
# 3.查找操作元素
driver.find_element(By.XPATH, "//*[text='登录']").click()
driver.find_element(By.XPATH, "//*[@placeholder='手机号/邮箱']").send_keys("16656009999")
driver.find_element(By.XPATH, "//*[contains(@placeholder,'密')]").send_keys("123456")
driver.find_element(By.XPATH, "//*[@placeholder='验证码' and @name='verify_code')]").send_keys("8888")
driver.find_element(By.XPATH, "//*[@class='login_button']/a").click()

# 4.关闭浏览器
sleep(2)
driver.quit()
