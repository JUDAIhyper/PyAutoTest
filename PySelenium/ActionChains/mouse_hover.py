#模拟用户事件
#执行原理：将用户操作放入perform队列中，按顺序调用
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间
sleep(3)
#定位鼠标移动到上面
menu_ele = driver.find_element_by_css_selector(
    "#app > div > div.main > div.banner.w > div.l_course_list > ul > li:nth-child(1)")
ActionChains(driver).move_to_element(menu_ele).perform()
#选中子菜单
sub_menu_ele = driver.find_element_by_css_selector(
    "#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(2)")
sleep(2)
sub_menu_ele.click()