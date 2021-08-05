from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack

from mysqlbank import Bank

'''
    DDT:data driver test
        ddt
        data
        unpack
    1.测试类必须用@ddt修饰
    2.测试方法使用@data引入数据源
    任务：
        将工行系统的核心业务进行测试？
        bank_addUser()

'''

# 数据源
# 添加用户数据
addUser = [
    [1, 1, 123456, 1, 1, 1, 1, 111111, None],
    [2, 1, 123456, 1, 1, 1, 1, 111111, None]
]
# 存钱数据
saveMoney = [
    [1, 111]
]
# 取钱数据
drawMoney = [
    [1, 123456, 1]
]
# 转账数据
transferMoney = [
    [1, 2, 123456, 1]
]
# 用户查询数据
userQuery = [
    [1, 123456]
]


@ddt  # 注解，注释这个类是参数化类
class TestBank(TestCase):
    # 添加用户测试
    @data(*addUser)  # 引入数据源
    @unpack  # 拆分数据源
    def testAddUser(self, account, username, password, country, province, street, gate, money, registerDate):
        # 2.调用被测方法
        bank = Bank()
        bank.bank_addUser(account, username, password, country, province, street, gate, money, registerDate)

    # 存钱测试
    @data(*saveMoney)  # 引入数据源
    @unpack  # 拆分数据源
    def testSaveMoney(self, account, sm):
        bank = Bank()
        bank.bank_saveMoney(account, sm)

    # 取钱测试
    @data(*drawMoney)  # 引入数据源
    @unpack  # 拆分数据源
    def testDrawMoney(self, account, pwd, dm):
        bank = Bank()
        bank.bank_drawMoney(account, pwd, dm)

    # 转账测试
    @data(*transferMoney)  # 引入数据源
    @unpack  # 拆分数据源
    def testTransferMoney(self, account, intoAccount, pwd, tm):
        bank = Bank()
        bank.bank_transferMoney(account, intoAccount, pwd, tm)

    #  用户查询测试
    @data(*userQuery)  # 引入数据源
    @unpack  # 拆分数据源
    def testUserQuery(self, account, pwd):
        bank = Bank()
        bank.bank_userQuery(account, pwd)
