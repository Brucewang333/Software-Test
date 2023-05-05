# 导包
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取浏览器
driver = webdriver.Chrome()
# 打开url
driver.get("file:///Users/lgy/Documents/fodder/web/Register.html")
# 隐式等待
driver.implicitly_wait(10)

'''
    页面注册A在iframe标签中，验证不处理是否能操作
'''
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys('admin')

'''
如何操作？
1、切换到iframe driver.switch_to.frame(iframe元素)
2、操作元素
3、回到默认⻚⾯ driver.switch_to.default_content()
'''

# 获取注册A iframe元素
A = driver.find_element(By.CSS_SELECTOR, "#iframe1")
# 切换到A
driver.switch_to.frame(A)
# 注册A
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys('admin')

# 回到默认⻚⾯
driver.switch_to.default_content()

# 获取注册B
B = driver.find_element(By.CSS_SELECTOR, '#iframe2')
# 切换到B
driver.switch_to.frame(B)
# 操作B
driver.find_element(By.CSS_SELECTOR, '#userB').send_keys('admin')

# 关闭浏览器
sleep(3)
driver.quit()