from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///Users/lgy/Documents/fodder/web/%E6%B3%A8%E5%86%8CA.html")

# 绝对路径
driver.find_element(By.XPATH, value='/html/body/form/div/fieldset/center/p[1]/input').send_keys("admin")

# 暂停两秒
sleep(2)
# 清除内容

# 相对路径
driver.find_element(By.XPATH, value='//fieldset//p[1]/input').send_keys("123")

# 单属性定位
driver.find_element(By.XPATH, "//input[@type='submit']").send_keys("123")
# 多属性定位
driver.find_element(By.XPATH, "//input[@value='提交' and @class='banana']").send_keys("123")

# 先定位到其父级元素，然后再找到该元素
driver.find_element(By.XPATH, "//div[@id='test1']/input[@value='提交']").send_keys("123")

# 利用元素的文本定位元素
driver.find_element(By.XPATH, "//*[text()='注册']").send_keys("admin")

# 利用局部属性值定位元素
driver.find_element(By.XPATH, "//*[contains(@attribute,'账号')]").send_keys("admin")

sleep(2)
driver.quit()

# //*[@属性名='属性值' and @属性名 = '属性值']
# //*[@type = "subnit"]
# //*[text() = "文本值"]   根据显示文本定位
# //父标签/子标签  必须直属子级
# //父标签[@属性='值']//后代标签   父和后代之间可以跨越元素
# //*[contains(@属性名,'属性部分值')]   属性值模糊匹配
