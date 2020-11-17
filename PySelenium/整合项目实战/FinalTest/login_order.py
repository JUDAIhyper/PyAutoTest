from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url="https://xdclass.net"
        self.driver.get(self.base_url)

    def tearDown(self):
        print("测试结束")
        pass
        #单个测试用例结束

    def test_login_order(self):
        u"登录测试用例"
        driver=self.driver
        #登录框
        login_ele = driver.find_element_by_css_selector(
            "#app > div > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)")
        ActionChains(driver).click(login_ele).perform()
        sleep(2)
        #输入账号密码
        driver.find_element_by_css_selector(
            "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").send_keys("phonenum")
        driver.find_element_by_css_selector(
            "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").clear()
        driver.find_element_by_css_selector(
            "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").send_keys("password")
        #查找登录按钮
        login_btn = driver.find_element_by_css_selector(
            "#app > div > div.header > div.main > div.login > div > div.login_btn > button")
        login_btn.click()
        sleep(2)
        #判断登录成功
        user_info_ele = driver.find_element_by_css_selector(
            "#app > div > div.header > div.r_userinfo.f_r > div.avatar.f_r > img")
        #触发hover事件
        ActionChains(driver).move_to_element(user_info_ele).perform()
        #获取用户名的元素
        user_name_ele = driver.find_element_by_css_selector(
            "#app > div > div.header > div.nav_container > div > div > div.user > p")
        print("=====测试结果=====")
        print(user_name_ele.text)
        video_ele = driver.find_element_by_css_selector(
            "#app > div > div.hot > div > div.content > a:nth-child(1) > div > h1")
        video_ele.click()
        sleep(2)
        #购买页面
        handles = driver.window_handles  # 获取当前浏览器的所有窗口句柄
        driver.switch_to.window(handles[-1])  # 切换到最新打开的窗口
        buy_btn = driver.find_element_by_css_selector(
            "#app > div > div.details_container.clearfix > div.body.w > div.r_container.f_r > div.gostudy > div.buy_tolearn > a")
        buy_btn.click()
        print("进入下单页面")
        sleep(5)
        driver.close()

if __name__=="__main__":
    unittest.main()
