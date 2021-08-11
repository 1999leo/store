from selenium import webdriver
import time

# 注册
driver = webdriver.Chrome()
driver.get('http://localhost:8080/HKR')
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[1]').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('羽12')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys("夏")
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="valid_age"]').send_keys('22')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/select[1]').send_keys('男')
driver.find_element_by_xpath('//*[@id="classname"]').send_keys('测试开发')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/input[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys('1483134716@qq.com')
driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys('15326463316')
driver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys('')
driver.find_element_by_xpath('//*[@id="btn_reg"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[3]/a').click()


# 登录
driver.get('http://localhost:8080/HKR')
# 输入用户名
driver.find_element_by_xpath("//*[@id='loginname' and @name='loginname' and @type='text']").send_keys("root")
# 输入密码
driver.find_element_by_xpath("//*[@id='password' and @name='password' and @type='password']").send_keys("root")
# 登陆
driver.find_element_by_xpath("//*[@id='submit' and @type='submit' and @value='登陆']").click()
# 换头像
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@title='小海豹']").click()

# 跳转首页
driver.find_element_by_xpath("//*[@id='tt']").click()
time.sleep(1)
driver.refresh()
# 评价表
# driver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9（上晚自习）")
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("7（没有晚自习）")
driver.find_element_by_xpath("//*[@name='teaName' and @class='show_tea']").send_keys("曹士明")
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='textarea']").send_keys("很好")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()
time.sleep(1)
# 跳转修改信息页面
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
# 修改信息
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("")
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("10")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("男")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").clear()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']  /table/tbody/tr[6]/td[2]/input").send_keys("北京")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys("")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("hello")
# driver.find_element_by_xpath("//*[@id='btn_modify']").click()
# time.sleep(3)
# driver.quit()
