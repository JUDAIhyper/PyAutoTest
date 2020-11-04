from logging import log
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间
sleep(2)
#登录框
login_ele=driver.find_element_by_css_selector(
    "#app > div > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)")
ActionChains(driver).click(login_ele).perform()
sleep(2)
#输入账号密码
driver.find_element_by_css_selector(
    "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").clear()
driver.find_element_by_css_selector(
    "#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").send_keys("phone")
driver.find_element_by_css_selector(
    "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").clear()
driver.find_element_by_css_selector(
    "#app > div > div.header > div.main > div.login > div > div.psw > input[type=password]").send_keys("password")
#查找登录按钮
login_btn=driver.find_element_by_css_selector(
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
name=user_name_ele.text
if name==u"username":
    print("SUCCESS")
else:
    print("FAIL")
