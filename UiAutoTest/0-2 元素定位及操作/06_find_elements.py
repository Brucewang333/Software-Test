'''
查找⼀组元素
说明：返回列表格式，要使⽤需要添加下标或遍历。
⽅法： driver.find_elements(By.xxxx,value='xxxx')
提示： ⼋⼤元素定位⽅法，都可以使⽤⼀组元素定位,如果没有搜索到符合标签，返回空
列表。
'''


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///Users/lgy/Documents/fodder/web/%E6%B3%A8%E5%86%8CA.html")

inputs = driver.find_elements(By.TAG_NAME, value="input")
inputs[0].send_keys("admin")
inputs[1].send_keys("123456")
inputs[2].send_keys("16600001234")
inputs[3].send_keys("123163@com")

# for input in inputs:
#     print(input)
    # input.send_keys("admin")
sleep(3)
driver.quit()
