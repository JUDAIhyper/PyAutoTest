from logging import log
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://xdclass.net")
print(driver.title)
#设置睡眠时间
sleep(2)
#登录框
login_ele=driver.find_element_by_css_selector(
    "#app > div > div.header > div.r_userinfo.f_r > div.login > span:nth-child(2)")
ActionChains(driver).click(login_ele).perform()
sleep(2)
#捕捉抓不到元素异常
try:
    driver.find_element_by_id("xdclass").click()
except:
    driver.get_screenshot_as_file("PySelenium//错误截图//error.png")
    
