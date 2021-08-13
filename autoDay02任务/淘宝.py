from selenium import webdriver
import time

# 创建一个谷歌驱动
driver = webdriver.Chrome()
# 打开页面
driver.get("https://www.taobao.com/")
# 窗口最大化
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div/div[2]/div[1]/a[1]').click()
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('15046463302')
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('xyp19990804')

driver.quit()