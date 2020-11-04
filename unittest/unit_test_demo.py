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
    def setUp(self):
        print("==selfUp==")
        
    def tearDown(self):
        print("--tearDown==")
        
    def test_name(self):
        print("==test_name==")
        
if __name__=="__main__":
    unittest.main()