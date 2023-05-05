from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1、打开⾕歌浏览器(实例化浏览器对象)
driver = webdriver.Chrome()
# 2、输⼊url
driver.get("http://tpshop-test.itheima.net/Home/user/login.html")
# 3、找元素及操作
# 1、获取浏览器
driver = webdriver.Chrome()
# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 最⼤化浏览器
driver.maximize_window()

# 获取当前窗⼝标题
print("当前窗⼝title：", driver.title)

# 获取当前窗⼝url
print("当前窗⼝url:", driver.current_url)
sleep(3)

driver.find_element(By.PARTIAL_LINK_TEXT, "注册A⽹⻚").click()
# 获取当前窗⼝标题
print("当前窗⼝title：", driver.title)

# 获取当前窗⼝url
print("当前窗⼝url:", driver.current_url)
sleep(3)

# 关闭当前窗内⼝
driver.close()

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
