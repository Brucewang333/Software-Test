# 1.导包
import unittest

import app
from script.test_index import TestIndex
from script.test_order import TestOrder
from script.test_product import TestProduct
from script.test_user import TestUser
from unittestreport import TestRunner

# 2.创建测试套件对象
suite = unittest.TestSuite()
# 3.添加测试用例到套件
suite.addTest(unittest.makeSuite(TestIndex))
suite.addTest(unittest.makeSuite(TestProduct))
suite.addTest(unittest.makeSuite(TestUser))
suite.addTest(unittest.makeSuite(TestOrder))
# 4.批量执行测试用例
runner = unittest.TextTestRunner()  # 实例化执行器对象
runner.run(suite)
# 5.生成测试报告
# 5.1 定义测试报告文件
rep_file = app.BASE_DIR + '/report/ego.html'
# 5.2 创建第三方执行器对象(手动导包)
runner = TestRunner(suite,
                    filename=rep_file,  # 测试套件对象
                    report_dir="./reports",  # 报告文件
                    title='ego微商接口测试报告',  # 报告标题
                    tester='Bruce',  # 测试执行人
                    desc="ego微商接口项目测试生成的报告",  # 报告描述信息
                    templates=1  # 报告的模板
                    )
# 5.3 执行器调用run方法执行生成报告
runner.run()
