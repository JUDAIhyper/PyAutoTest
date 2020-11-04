"""
需求：
    1.利用unittest执行流程测试而非单元测试
    2.控制unittest的执行顺序

1.unittest.TestSuite() 类来表示一个测试用例集
    1）用来确定测试用例的顺序，哪个先执行哪个后执行
    2）如果一个class中有四个test开头的方法，则加载到suite中时则有四个测试用例
    3）由TestLoader加载TestCase到TestSuite
    4）verbosity参数可以控制执行结果的输出，0 是简单报告，1 是一般报告， 2 是详细报告
        默认1 会在每个成功的用例前面有个"." 每个失败的用例前面有个 "F"

2.TextTestRunner() 文本侧是用例运行器

3.run()方法是运行测试套件的测试用例，入参为suite测试套件
"""
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.age=12
        self.name="python自动化"
        print(" setUp method=======")
        
    def tearDown(self):
        print(" tearDown method======")
        #断言是否相同
        self.assertEqual("foo".upper(),"FOO")
        
    def test_one(self):
        print(" test_one 第一个测试用例")
        #断言是否相同
        self.assertEqual(self.name,"python自动化",msg="名字不对")
        
    def test_two(self):
        print(" test_two 第二个测试用例")
        #断言是否为true，msg是断言错误的提示信息
        self.assertFalse("PYTHON".isupper(),msg="不是大写") 
        
    def test_three(self):
        print(" test_three 第三个测试用例")
        self.assertEqual(self.age,32)

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(MyTestCase("test_one"))
    suite.addTest(MyTestCase("test_two"))
    suite.addTest(MyTestCase("test_three"))
    runner=unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
