from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("华为mate40")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_01:0070094634_12199717163"]/i/img').click()
time.sleep(1)
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()

time.sleep(1)
driver.close()
driver.quit()