from time import sleep

from selenium import webdriver

driver = webdriver.Chrome

driver.get("https://www.baidu.com")

'''
说明： 由服务器⽣成，存储在客户端的登录凭证
使⽤：
1、获取cookie # 获取所有driver.get_cookies()
2、添加cookie # driver.add_cookie(data)
'''

data = {"name": "BDUSS",
        "values": "01TnVCUTZscnV3ZDZQZXhndEVsSFcxbUFmNUtHVmFXbUgzQmtZVU9RNk1XbFZqSVFBQUFBJCQAAAAAAAAAAAEAAAB3IalesKKx8rK7yseworH2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIzNLWOMzS1jeU"}

driver.add_cookie(data)

sleep(3)

driver.refresh()
sleep(3)
driver.quit()