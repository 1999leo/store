import random

# 1.准备一个数据库和银行名称
# 空的数据库
bank = {}

bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
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
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if account in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,  # 用户名
        "password": password,  # 密码
        "country": country,  # 国家
        "province": province,  # 省
        "street": street,  # 街道
        "gate": gate,  # 门
        "money": money,  # 钱
        "bank_name": bank_name  # 银行名
    }
    return 1


# 银行的存钱逻辑
def bank_saveMoney(account, sm):
    # 判断是否在字典中
    if account not in bank:
        return False
    bank[account]["money"] = sm + bank[account]["money"]



# 银行的取钱逻辑
def bank_drawMoney(account, pwd, dm):
    # 判断账户是否在字典中
    if account not in bank:
        return 1
    # 判断账户密码对错
    if pwd != bank[account]["password"]:
        return 2
    # 判断取款金额是否大于余额
    if dm > bank[account]["money"]:
        return 3


# 银行的转账逻辑
def bank_transferMoney(account, intoAccount, pwd, tm):
    # 判断转出账户是否在字典中
    if account not in bank:
        return 1
    # 判断转入账户是否在字典中
    if intoAccount not in bank:
        return 1
    # 判断转出账户密码的对错
    if pwd != bank[account]['password']:
        return 2
    # 判断转账金额大于转出账户的余额
    if tm > bank[account]['money']:
        return 3


# 银行的查询逻辑
def bank_userQuery(account, pwd):
    if account not in bank:
        print('您输入的账号不存在！')
    else:
        if pwd != bank[account]['password']:
            print('您输入的密码不正确！')
        else:
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
                        ---------------------------
                    '''
            print(info % (bank[account]['username'], bank[account]['password'], account, bank[account]['country'],
                          bank[account]['province'], bank[account]['street'], bank[account]['gate'],
                          bank[account]['money'], bank_name))


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

    status = bank_addUser(account, username, password, country, province, street, gate, money)

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
            --------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


# 用户的存钱操作逻辑
def saveMoney():
    account = input('请输入您的账号：')
    if account.isdigit():
        account = int(account)
        sm= input('请输入您要存入的金额：')
        if sm.isdigit():
            sm = int(sm)
            data = bank_saveMoney(account, sm)
            if data == False:
                print('账号不存在！')
            else:
                print('存钱成功，您当前余额为', bank[account]['money'], '元！')
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
                drawMoney()
            elif data == 2:
                print("您输入的密码错误！")
                drawMoney()
            elif data == 3:
                print("您的账号余额不足！")
                drawMoney()
            else:
                bank[account]["money"] = bank[account]["money"] - dm
                print("取钱成功，您的当前余额为:", bank[account]["money"], "元！")
        else:
            print("金额输入错误，请重新输入！")
            drawMoney()
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
                transferMoney()
            elif data == 1:
                print('您要转入的账号不存在！')
                transferMoney()
            elif data == 2:
                print('您输入的密码不正确！')
                transferMoney()
            elif data == 3:
                print('您的账号余额不足！')
                transferMoney()
            else:
                bank[account]['money'] = bank[account]['money'] - tm
                bank[intoAccount]['money'] = bank[intoAccount]['money'] + tm
                print('转账成功，您的账号当前余额为：', bank[account]['money'], '元！')
        else:
            print('您输入的要转入的账号格式错误！')
            transferMoney()
    else:
        print('您输入的账号格式错误！')
        transferMoney()


# 用户的查询操作逻辑
def userQuery():
    account = input('请输入您的账号:')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码:')
        pwd = int(pwd)
        bank_userQuery(account, pwd)
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
