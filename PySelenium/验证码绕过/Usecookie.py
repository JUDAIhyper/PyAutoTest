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
driver.add_cookie({"name": "name", "value":"judaiplus233"})
driver.add_cookie({"name": "token", "value": "xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMTcuanBlZyIsImlkIjo2NzgwNjkxLCJuYW1lIjoianVkYWlwbHVzMjMzIiwiaWF0IjoxNjA0MzI1NTE1LCJleHAiOjE2MDQ5MzAzMTV9.y2COME5VTaTRRHcdtZMEnTkW9K8ONsoI6eZZlr5IJ3I"})
video_ele = driver.find_element_by_css_selector(
    "#app > div > div.new > div > div.content > div.l_content > a:nth-child(1) > div")
video_ele.click()
sleep(2)
