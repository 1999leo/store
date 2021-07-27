import random
import time

import pymysql

# 准备一个数据库和银行名称
# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="root", database="bank")

# 2.创建控制台
cursor = con.cursor()

# 银行名称
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行            *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money, registerDate):
    # 1.判断数据库是否已满
    cursor.execute("SELECT * from user")
    record = cursor.fetchall()
    if len(record) >= 100:
        return 3
    else:
        # 2.判断用户是否存在
        cursor.execute("SELECT * from user where account = %s" % account)
        record1 = cursor.fetchone()
        if record1 is not None:
            return 2
        else:
            # 3.正常开户
            sql = "insert into  user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            a = [account, username, password, country, province, street, gate, money, bank_name, registerDate]
            cursor.execute(sql, a)
            con.commit()
            return 1


# 银行的存钱逻辑
def bank_saveMoney(account, sm):
    cursor.execute("SELECT account FROM `user` where account = %s " % account)
    record = cursor.fetchone()
    # 判断是否存在数据库中
    if record is None:
        return False
    else:
        sql = "UPDATE `user` SET money=money+%s WHERE account=%s "
        data = [sm, account]
        cursor.execute(sql, data)  # (模板, 参数)
        con.commit()


# 银行的取钱逻辑
def bank_drawMoney(account, pwd, dm):
    # 判断账户是否在字典中
    cursor.execute("SELECT * FROM `user` where account = %s" % account)
    record = cursor.fetchone()
    if record is None:
        return 1
    if record[2] != pwd:
        return 2
    if record[7] < dm:
        return 3
    sql = "UPDATE `user` SET money = money - %s WHERE account = %s"
    data = [dm, account]
    cursor.execute(sql, data)
    con.commit()


# 银行的转账逻辑
def bank_transferMoney(account, intoAccount, pwd, tm):
    cursor.execute("SELECT * FROM `user` where account = %s" % account)
    record = cursor.fetchone()
    # 判断账户是否在数据库中
    if record is None:
        return 1
    # 判断转出账户密码的对错
    elif record[2] != pwd:
        return 2
    # 判断转账金额大于转出账户的余额
    elif record[7] < tm:
        return 3
    else:
        sql = "UPDATE `user` SET money=money-%s WHERE account=%s "
        sql1="UPDATE `user` SET money=money+%s WHERE account=%s "
        data = [tm, account]
        data1 = [tm, intoAccount]
        cursor.execute(sql, data)
        cursor.execute(sql1,data1)
        con.commit()

# 银行的查询逻辑
def bank_userQuery(account, pwd):
    cursor.execute("SELECT * FROM `user` where account = %s" % account)
    record = cursor.fetchone()

    if record is None:
        print('您输入的账号不存在！')
    else:
        if record[2] != pwd:
            print('您输入的密码不正确！')
        else:
            sql = "SELECT * FROM `user` WHERE account=%s AND `password`=%s"
            data = [account, pwd]
            cursor.execute(sql, data)  # (模板, 参数)
            con.commit()
            print('查询成功，您的个人信息如下:')
            info = '''
                        ----------个人信息----------
                        用户名：%s
                        密码：%s
                        账号：%s
                        地址信息
                            国家：%s
                            省份：%s
                            街道：%s
                            门牌号: %s
                        余额：%s
                        开户行地址：%s
                        注册日期：%s
                        ---------------------------
                    '''
            print(info % (record[1], record[2], record[0], record[3], record[4], record[5], record[6], record[7],
                          record[8], record[9]))


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    while True:
        password = input("请输入您的开户密码：")
        if len(password) != 6:
            print("密码为6位,请重新输入!")
        else:
            # 判断是否是个数字,如果是则强转为整形
            if password.isdigit():
                password = int(password)
                break
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    while True:
        money = input("请输入您的开户初始余额：")
        # 判断是否是个数字,如果是则强转为整形
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入非法,重新输入")
    account = random.randint(10000000, 99999999)  # 随机产生8为数字
    registerDate = time.strftime('%Y-%m-%d %H:%M:%S')  # 获取系统时间
    status = bank_addUser(account, username, password, country, province, street, gate, money, registerDate)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息----------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            注册日期：%s
            --------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name, registerDate))


# 用户的存钱操作逻辑
def saveMoney():
    account = input('请输入您的账号：')
    if account.isdigit():
        account = int(account)
        sm = input('请输入您要存入的金额：')
        if sm.isdigit():
            sm = int(sm)
            data = bank_saveMoney(account, sm)
            if data == False:
                print('账号不存在！')
            else:
                cursor.execute("SELECT * FROM `user` where account = %s " % account)
                record = cursor.fetchone()

                print('存钱成功，您当前余额为', record[7], '元！')
        else:
            print('金额输入错误，请重新输入！')
    else:
        print('账号格式输入错误，请重新输入！')
        saveMoney()


# 用户的取钱操作逻辑
def drawMoney():
    account = input("请输入您的账号:")
    if account.isdigit():
        account = int(account)
        pwd = int(input("请输入您的密码:"))
        dm = input("请输入您要提取的金额:")
        if dm.isdigit():
            dm = int(dm)
            data = bank_drawMoney(account, pwd, dm)
            if data == 1:
                print("您输入的账号不存在！")
            elif data == 2:
                print("您输入的密码错误！")
            elif data == 3:
                print("您的账号余额不足！")
            else:
                cursor.execute("SELECT * FROM `user` where account = %s" % account)
                record = cursor.fetchone()
                li = [record]
                print('取钱成功，您的当前余额为', record[7], '元！')
        else:
            print("金额输入错误，请重新输入！")
    else:
        print("账号输入错误，请重新输入！")
        drawMoney()


# 用户的转账操作逻辑
def transferMoney():
    account = input('请输入您的转出账号：')
    if account.isdigit():
        account = int(account)
        intoAccount = input('请输入您的转入账号：')
        if intoAccount.isdigit():
            intoAccount = int(intoAccount)
            pwd = int(input('请输入您的密码：'))
            tm = int(input('请输入您要转的金额：'))
            data = bank_transferMoney(account, intoAccount, pwd, tm)
            if data == 1:
                print('您输入的账号不存在！')
            elif data == 2:
                print('您输入的密码不正确！')
            elif data == 3:
                print('您的账号余额不足！')
            else:
                cursor.execute("SELECT * FROM `user` where account = %s" % account)
                record = cursor.fetchone()
                li = [record]
                print('转账成功，您的账号当前余额为：', record[7], '元！')
        else:
            print('您输入的要转入的账号格式错误！')
    else:
        print('您输入的账号格式错误！')
        transferMoney()


# 用户的查询操作逻辑
def userQuery():
    account = input('请输入您的账号:')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码:')
        if pwd.isdigit():
            pwd = int(pwd)
            bank_userQuery(account, pwd)
        else:
            print("密码必须为纯数字!")
    else:
        print('账号格式输入错误！')
        userQuery()


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoney()
    elif chose == "3":
        drawMoney()
    elif chose == "4":
        transferMoney()
    elif chose == "5":
        userQuery()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
cursor.close()
con.close()
