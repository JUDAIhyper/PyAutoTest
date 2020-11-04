"""
1.用import语句引入unittest模块
2.测试的类都继承于TestCase类
3.setUp() 测试前的初始化工作：testDown()测试后的清除工作(在每个测试方法运行时被调用)
注意：
    1.所有类中方法的入参为self，定义方法的变量也要self.变量
    2.定义测试用例，以"test"开头命名的方法，方法的入参为self
    3.unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行他们
    4.自己写的py文件不能用unittest.py命名，不然会找不到TestCase
    成功是输出，失败是F
"""
import unittest

class UserTestCase(unittest.TestCase):
    def tearDown(self):
        print("==tearDown==")
        
    def setUp(self):
        print("==selfUp==")
        self.name="python自动化"
        
    def test_name(self):
        print("调用test_name")
        print(self.name)
        #断言是否相同
        self.assertEqual(self.name,"python自动化",msg="名字不对")
    
    def test_isupper(self):
        print("调用test_isupper")
        #断言是否为true，msg是断言错误的提示信息
        self.assertTrue("xdclass".isupper(),msg="不是大写")
    
    def test_age(self):
        print("调用test_age")
        
if __name__=="__main__":
    unittest.main()