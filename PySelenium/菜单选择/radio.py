from selenium import webdriver
from time import sleep
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("PyAutoTest\\PySelenium\\菜单选择\\radio.html")
print(driver.title)
print("默认选中male")
#2秒后选择female
sleep(2)
driver.find_element_by_id("female").click()