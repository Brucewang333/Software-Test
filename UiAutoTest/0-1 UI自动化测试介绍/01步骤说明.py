from time import sleep
from selenium import webdriver
# 1、打开⾕歌浏览器(实例化浏览器对象)
driver = webdriver.Chrome()
# 2、输⼊url
driver.get("http://tpshop-test.itheima.net/Home/user/login.html")
# 3、找元素及操作


# 4、关闭浏览器
sleep(3)
driver.quit()