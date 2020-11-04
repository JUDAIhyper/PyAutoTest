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