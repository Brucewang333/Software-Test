# 1.导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# 2.创建浏览器对象,打开浏览器
driver = webdriver.Chrome
driver.get("http://hmshop-test.itheima.net/")
# 3.查找操作元素

# 属性选择器 语法: [属性名='属性值']
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys('admin')

# 类选择器 语法： .class属性值
driver.find_element(By.CSS_SELECTOR, "[name='passwordA']").send_keys("123456")

# 类选择器 语法： .class属性值
driver.find_element(By.CSS_SELECTOR, ".telA").send_keys("16656006666")

# 标签选择器 语法： 标签名
driver.find_element(By.CSS_SELECTOR, "button").click()

# CSS定位-层级选择器  父子关系：element1>element2
#                   后代关系：element1 element2

# 利用局部属性值定位元素
driver.find_element(By.CSS_SELECTOR,"[placeholder*='账']").send_keys("admin")

# 4.关闭浏览器
sleep(2)
driver.quit()
