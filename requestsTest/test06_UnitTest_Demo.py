import unittest


# 待测试方法
def add(x, y):
    return x + y


# 封装测试类 从UnitTest.TestCase继承
class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        print("----setup-----")

    def tearDown(self) -> None:
        print("----teardown----")
    @classmethod
    def setUpClass(cls) -> None:
        print("=====setUpClass====")
    @classmethod
    def tearDownClass(cls) -> None:
        print("====tearDown====")

    # 自定义方法
    def test_01_add(self):
        ret = add(10, 20)
        self.assertEqual(30, ret)

