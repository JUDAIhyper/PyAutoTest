import unittest
import HTMLTestRunner
import time
import os

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.age = 12
        self.name = "python自动化"
        print(" setUp method=======")

    def tearDown(self):
        print(" tearDown method======")
        #断言是否相同
        self.assertEqual("foo".upper(), "FOO")
    #添加测试说明
    def test_one(self):
        u"test_one方法说明"
        print(" test_one 第一个测试用例")
        #断言是否相同
        self.assertEqual(self.name, "python自动化", msg="名字不对")

    def test_two(self):
        u"test_two方法说明"
        print(" test_two 第二个测试用例")
        #断言是否为true，msg是断言错误的提示信息
        self.assertFalse("PYTHON".isupper(), msg="不是大写")

    def test_three(self):
        u"test_three方法说明"
        print(" test_three 第三个测试用例")
        self.assertEqual(self.age, 32)
        
    def test_four(self):
        u"test_four方法说明"
        print(" test_four 第四个测试用例")
        self.assertEqual(self.name,12) 


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_one"))
    suite.addTest(MyTestCase("test_two"))
    suite.addTest(MyTestCase("test_three"))
    suite.addTest(MyTestCase("test_four"))
    # runner = unittest.TextTestRunner(verbosity=1)
    # runner.run(suite)
    file_prefix=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    print(file_prefix)
    #创建测试报告    
    fp = open("PyAutoTest\\PySelenium\\TestSuite\\"+file_prefix+"_result.html", "wb")
    #定义测试报告写入的文件
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"网页测试报告",description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()
