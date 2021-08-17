import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

sender = '1483221745@qq.com'  # 发件人邮箱账号
my_pass = 'dbwjyawvukmeffdj'  # 发件人邮箱授权码
user = '2431320433@qq.com'  # 收件人邮箱账号


msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(("夏云鹏", sender))  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(("", user))  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

# 发送附件
att = MIMEText(open('TestingReport.html', 'rb').read(), 'base64',
               'utf-8')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=TestingReport.html"  # filename为文件名字
msg.attach(att)

# 以附件形式发送图片
tests = os.getcwd()
for i in os.listdir(tests):
    if '.png' in i:
        targetPath = os.path.join(tests, i)
        Image = MIMEImage(open(targetPath, 'rb').read())  # 图片的路径
        Image["Content-Type"] = 'image/jpg'
        Image["Content-Disposition"] = "attachment; filename=loginFailed.jpg"
        msg.attach(Image)
    else:
        continue

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    server.quit()  # 关闭连接
    print("邮件发送失败")
