from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1、打开⾕歌浏览器(实例化浏览器对象)
driver = webdriver.Chrome()
# 2、输⼊url
driver.get("http://tpshop-test.itheima.net/Home/user/login.html")
# 3、找元素及操作
driver.maximize_window()
sleep(3)

driver.set_window_size("500px", "700px")
sleep(3)

driver.set_window_position("x=0px", "y=500px")
sleep(3)

driver.find_element(By.PARTIAL_LINK_TEXT, "百度").click()
sleep(3)

driver.back()
sleep(3)

driver.forward()
sleep(3)

driver.refresh()

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
