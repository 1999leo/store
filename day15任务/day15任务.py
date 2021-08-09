"""
以下文件是用户的一些数据（姓名、年龄、净资产），要求使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！
贾生,47,50000
马云,58,1000000
马化腾,57,1000202
付光旭,20,560304
穆子康,24,230023
杜会朦,25,204892

"""
import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', database='people')
cursor = con.cursor()
user = open(file='用户数据.txt', mode='r+', encoding='utf-8')
assets = 0
for i in range(6):
    data = user.readline()
    a = data.split(",", 2)
    sql = 'insert into user values(%s,%s,%s)'
    param = [a[0], a[1], a[2]]
    assets += int(a[2])
    cursor.execute(sql, param)
print('资产总额为:', assets)
con.commit()
cursor.close()
con.close()
user.close()
"""
    使用python复制一张图片到D盘的python文件夹里
"""

photo = open(file="布偶.jpeg", mode="rb")
photo1 = open(file=r"D:\PycharmProjects\pythonProject\day15\day15任务\布偶猫.jpeg", mode="wb")
data = photo.read()
photo1.write(data)
photo1.flush()
photo1.close()
photo.close()

"""
    编写程序模拟证件上传的功能，让用户输入证件的路径，并拷贝到一个统一的图片路径下。
"""
address = input("请输入证件的路径")
photo2 = open(file="{}".format(address), mode="rb")
photo3 = open(file=r"D:\PycharmProjects\pythonProject\day15\day15任务\{}".format(address), mode="wb")
data = photo2.read()
photo3.write(data)
photo3.flush()
photo3.close()
photo2.close()

"""
    编程实现：有names.txt文件，实现用户的注册，登陆，修改密码，上传头像并记录头像路径的功能。（选做）
"""
li = []
print("------用户注册------")
li.append(input("请输入姓名："))
li.append(input("请输入密码："))
li.append(input("请输入性别："))
li.append(input("请输入年龄："))
li.append(input("请输入地址："))
li.append(input("请输入头像路径："))

register = open(file="Names.txt", mode="a+", encoding="utf-8")
length = len(li)
for i in range(length):
    if length - i != 1:
        register.write(li[i] + ",")
    else:
        register.write(li[i])
register.write("\n")
register.flush()
register.close()
"""
现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。
"""
file = (open('scores.txt', 'r+', encoding='utf-8')).readlines()
rows2 = len(file)  # 获取行数
fraction = 0
for i in range(rows2):
    cols = len(file[i])  # 获取列数
    part = file[i].split(' ', cols)  # 进行分割
    col = len(part)  # 获取列数
    for j in range(1, col):
        count = int(part[j])
        fraction += count
(open('scores1.txt', 'a', encoding='utf-8')).write('总得分为：' + str(fraction))

"""
 任务需求:
        统计每个Ip地址出现的次数

"""
f = open(file="baidu_x_system.log", mode="r", encoding="utf-8")
data = f.readlines()
frequency = dict()
for value in data:
    t = value.split(" ", 1)[0]
    if t in frequency:
        frequency[t] += 1
    else:
        frequency[t] = 0
print(frequency)
f.close()
