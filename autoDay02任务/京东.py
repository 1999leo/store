
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.jd.com")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="J_user"]/div/div[1]/div[2]/p/a[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()

driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('15046463302')
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('Xyp19990804')
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
time.sleep(5)
# 搜索华为Mate40
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为mate40")
time.sleep(1)
driver.find_element_by_class_name("button").click()
time.sleep(1)
# 选择商品
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
time.sleep(1)

data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
driver.find_element_by_xpath('//*[@id="GotoShoppingCart"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a/b').click()
# 关闭服务
driver.close()
# 关闭浏览器
driver.quit()