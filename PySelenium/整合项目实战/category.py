import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class CategoryTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = "https://xdclass.net"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("测试结束")
        pass
        #单个测试用例结束
    
    def test_menu(self):
        u"弹出菜单测试用例"
        driver=self.driver
        #跳转网页
        sleep(1)
        #定位到鼠标移动到上面的元素
        menu_ele = driver.find_element_by_css_selector(
            "#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)")
        ActionChains(driver).move_to_element(menu_ele).perform()
        #选中子菜单
        sub_menu_ele = driver.find_element_by_css_selector(
            "#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(2)")
        sleep(2)
        sub_menu_ele.click()
        sleep(2)
        driver.close()

if __name__=="__main__":
    unittest.main()               
