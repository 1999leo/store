'''
    报告：
        1.加载器：加载所有测试用例并得到所有用例
        2.使用运行器运行这些测试用例并生成报告
    任务2：
        减乘除：进行测试（）
        实现报告的邮件发送
'''
from HTMLTestRunner import HTMLTestRunner  # 运行器
import unittest

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\pythonProject\day13\day13任务", pattern="test*.py")

# 2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    # 测试标题
    title="这是一份计算器的测试报告",
    # 子标题
    description="",
    # 处理详细程度
    verbosity=1,
    # 写入文件
    stream=open("计算器.html", mode="w+", encoding="utf-8")
)

# 3.运行所有用例
runner.run(tests)


# 4.实现邮件发送
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

sender = '1483221745@qq.com'  # 发件人邮箱账号
my_pass = 'hlfijrxzgbnlgffj'  # 发件人邮箱授权码
user = '1483221745@qq.com'  # 收件人邮箱账号


msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["墨白", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["墨白", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题
# 发件人邮箱中的SMTP服务器，SMTP端口是25
server = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 括号中对应的是发件人邮箱账号、邮箱密码
server.login(sender, my_pass)
# 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att = MIMEText(open('D:\PycharmProjects\pythonProject\day13\day13任务\计算器.html', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=case.html"  # filename为文件名字
msg.attach(att)

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")
