from selenium import webdriver
from time import sleep
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://xdclass.net")
print(driver.title)
#睡眠时间
sleep(3)
driver.find_element_by_xpath(
    '//*[@id="app"]/div/div[6]/div[3]/div/div[2]/a[1]/div').click()
