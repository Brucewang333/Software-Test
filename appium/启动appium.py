from appium import webdriver

# 定义字典变量
desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
# 注意：版本号必须正确
desired_caps["platformVersion"] = "7.1.1"
# android不检测内容，但是不能为空
desired_caps["deviceName"] = "192.168.56.101:5555"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
# 设置中⽂
desired_caps["nicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
