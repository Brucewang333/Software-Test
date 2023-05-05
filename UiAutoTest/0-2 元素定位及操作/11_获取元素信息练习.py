from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome
driver.get("http://hmshop-test.itheima.net/")

size = driver.find_element(By.CSS_SELECTOR, "#userA").size
print("用户名输入框的大小为:", size)

url_text = driver.find_element(By.TAG_NAME, "a").text
print("第一个超链接的文本内容为:", url_text)

a_href = driver.find_element(By.TAG_NAME, "a").get_attribute("href")
print("第一个超链接的地址为:", a_href)

span = driver.find_element(By.TAG_NAME, "span").is_displayed()
print("span是否可⻅:", span)

btn_is_enabled = driver.find_element(By.CSS_SELECTOR, "#cancelA").is_enabled()
print("取消按钮是否可⽤：", btn_is_enabled)

is_selected = driver.find_element(By.CSS_SELECTOR, "travelA").is_selected()
print("旅游是否被选中：", is_selected)

# //*[@属性名='属性值' and @属性名='属性值']    xpath策略 多个属性
# //[@属性名='值']/标签                       xpath策略 层级
