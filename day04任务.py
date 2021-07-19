'''
    需求：
        购物流程。
        1.商品在货架上
        2.空的购物车
        3.自己的初始化资金
    技术选型：
        1.容器
            列表： []
        2.循环技术
            while
            for i in  enumerate(li)
        3.判断
        5.键盘输入
    任务：
    [10张老干妈：7折优惠券，20张联想电脑1折优惠券]
    开始买东西之前，提示是否要抽一张优惠券。
        若是：随机给一张，最终要进行使用优惠券的进行结算。
        若否：正常买东西
'''

# 1.准备商品
import random

shop = [
    ["劳力士手表", 200000],
    ["Iphone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["HUA WEI WATCH", 1200],
    ["Mac PC", 15000],
    ["辣条", 2.5],
    ["老干妈", 10]
]
# 2. 初始化钱包
money = int(input("请输入您的余额："))

# 3.空的购物车
myCart = []
# 4.抽取购物券
coupon = random.randint(1, 30)
while True:
    extract = input("是否要抽取优惠券,y/n\n")
    if extract == "y":
        if coupon <= 10:
            print("恭喜你抽到一张7折老干妈优惠券!")
        elif coupon > 10:
            print("恭喜你抽到一张联想电脑1折优惠券!")
        break
    elif extract == "n":
        print("按原价购买商品!")
        break
    else:
        print("输入错误重新输入!")

# 电脑打折
discount1 = 0.1
# 老干妈打折
discount2 = 0.7

# 5.买东西
while True:
    # 5.1 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    # 5.2 请输入您想要的商品
    choose = input("亲输入您想要的商品编号：")  # "1"
    # 5.3 判断是不是个数字
    if choose.isdigit():
        choose = int(choose)
        # 5.4 先判断是否存在该商品
        if choose > 6:
            print("您输入的商品不存在！别瞎弄！")
        else:
            if extract == "y":
                # 5.5 判断您的余额是否足够
                if choose == 2 and coupon > 10 and money >= shop[choose][1] * discount1:
                    # 5.6 将商品添加到购物车 ，余额减去对应的钱
                    myCart.append(shop[choose])
                    money = money - int((shop[choose][1]) * discount1)
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif choose == 6 and coupon <= 10 and money >= shop[choose][1] * discount2:
                    # 5.6 将商品添加到购物车 ，余额减去对应的钱
                    myCart.append(shop[choose])
                    money = money - int((shop[choose][1]) * discount2)
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                elif money > shop[choose][1]:
                    myCart.append(shop[choose])
                    money = money - shop[choose][1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                else:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
            elif extract == "n":
                # 5.5 判断您的余额是否足够
                if money < shop[choose][1]:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
                    # 5.6 将商品添加到购物车 ，余额减去对应的钱
                    myCart.append(shop[choose])
                    money = money - shop[choose][1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
    elif choose == "q" or choose == "Q":
        print("拜拜了，您嘞！欢迎下次光临！")
        break
    else:
        print("对不起，您输入有误，请重新输入！")
# 打印购物小条
print("以下是您的购物小条，请拿好：")
for key, value in enumerate(myCart):
    print(key, value)
print("本次余额还剩：￥", money)
