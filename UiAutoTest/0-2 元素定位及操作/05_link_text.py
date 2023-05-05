from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///Users/lgy/Documents/fodder/web/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(by=By.TAG_NAME, value="input").send_keys("admin")

# link_text 全部值
driver.find_element(By.LINK_TEXT, value="新浪").click()

# partial_link_text
driver.find_element(By.PARTIAL_LINK_TEXT, value="新浪").click()

sleep(3)
driver.quit()
