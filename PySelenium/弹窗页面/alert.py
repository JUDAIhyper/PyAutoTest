from selenium import webdriver
from time import sleep
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("E:\\STUDY\\ownpython\\PyAutoTest\\PySelenium\\弹窗页面\\alert.html")
sleep(2)
driver.find_element_by_id("alert").click()
#弹窗常用方法(需要先切换窗口 switch_to_alert())
"""
accept() 表示接受
dismiss() 表示取消
"""
#切换窗口至弹窗
win=driver.switch_to_alert()
sleep(2)
win.accept()
sleep(2)
driver.find_element_by_id("confirm").click()
#切换弹窗
confirm_ele = driver.switch_to_alert()
sleep(2)
confirm_ele.dismiss()
