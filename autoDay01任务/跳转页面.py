from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get(r'D:\PycharmProjects\pythonProject\auto_day01\练习的html\跳转页面\pop.html')
# 窗口最大化
driver.maximize_window()
# 定位输入框
driver.find_element_by_id('goo').click()
time.sleep(3)
# 关闭浏览器
driver.quit()
