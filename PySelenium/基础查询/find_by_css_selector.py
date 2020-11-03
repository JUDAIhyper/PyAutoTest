from selenium import webdriver
from time import sleep
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间
sleep(3)
driver.find_element_by_css_selector(
    "#app > div > div.area > div:nth-child(3) > div > div.content > a:nth-child(1) > div > h1").click()

