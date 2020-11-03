from selenium import webdriver
#拿到driver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#选中输入框输入关键词
driver.find_element_by_id("kw").send_keys("python自动化测试")
driver.find_element_by_id("su").click()
#find_by_name
#find_by_class_name
driver.close()