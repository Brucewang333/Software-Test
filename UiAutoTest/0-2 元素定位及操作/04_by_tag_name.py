from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///Users/lgy/Documents/fodder/web/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(by=By.TAG_NAME, value="input").send_keys("admin")

sleep(3)
driver.quit()