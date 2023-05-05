from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1、获取浏览器
driver = webdriver.Chrome()

# 2、打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")

# 点击广州
# driver.find_element(By.CSS_SELECTOR, "[name='gz']").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "[name='sh']").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "[name='bj']").click()

# 使用Select类来实现
# 1.定位下拉框元素 select
el = driver.find_element(By.CSS_SELECTOR, "#selectA")

# 2.实例化Select对象
select = Select(el)

# 3.适用下标定位广州
select.select_by_index(2)
sleep(2)

# 使用value定位上海
select.select_by_value("sh")
sleep(2)
# 使用文本定位北京
select.select_by_visible_text("A北京")
# 关闭当前窗内⼝
driver.close()

# 4、关闭浏览器
sleep(3)
driver.quit()

# driver.close()  关闭当前窗口
