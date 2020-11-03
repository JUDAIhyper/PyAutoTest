from logging import log
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
#获取driver
driver = webdriver.Chrome()
#跳转
driver.get("https://www.baidu.com")
#显性等待
"""
WebDriverWait(driver,5,0.5) 最大等待时间和扫描间隔时间
完成对选择元素的寻找后执行下一步
"""
#异常处理
try:
    ele=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    ele.send_keys("python自动化")
    print(driver.title)
    print("资源加载成功")
except:
    print("资源加载失败，发送报警或邮件")
finally:
    print("不管有无成功，打印这句话，用于资源清理")
    #退出
    driver.quit()

# #隐性等待,最长等待10秒
# driver.implicitly_wait(10)
#隐性等待和显性等待可以同时用，等待的最长时间取两者中的较大者

