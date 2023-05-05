import unittest

from test06_UnitTest_Demo import TestAdd

from htmltestreport import HTMLTestReport

# 创建suite实例
suite = unittest.TestSuite()

# 指定测试类 添加测试方法
suite.addTest(unittest.makeSuite(TestAdd))

# 创建HTMLTestReport实例
runner = HTMLTestReport("测试报告.html")

# 调用run()
runner.run(suite)
