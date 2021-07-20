import random

# 1.准备商品
shop = [
    ["劳力士手表", 200000],
    ["Iphone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["HUA WEI WATCH", 1200],
    ["Mac PC", 15000],
    ["辣条", 2.5],
    ["老干妈", 10]
]

# 景区
data = {
    "北京": {
        "昌平": {
            "十三陵": ["十三陵水库", "沙河水库"],
            "高校": ["北京邮电大学", "中央戏剧学院", "北京师范大学", "华北电力大学", "北京航空航天大学"],
            "天通苑": ["海底捞", "呷哺呷哺"]
        },
        "海淀": {
            "公主坟": ["军事博物馆", "中华世纪园"],
            "科普场馆": ["中国科技馆", "北京天文馆"],
            "高校": ["北京大学", "清华大学"],
            "景区": ["北京植物园", "香山公园", "玉渊潭公园"]
        },
        "朝阳": {
            "龙城": ["鸟化石国家地质公园", "朝阳南北塔"],
            "双塔": ["朝阳凌河公园", "朝阳凤凰山"]
        },
        "延庆": {
            "龙庆峡": ["龙庆峡景区"]
        }
    }
}
# 电脑打折
discount1 = 0.1
# 老干妈打折
discount2 = 0.7

# 空的购物车
myCart = []

# 初始化钱包
money = int(input("请输入您的旅游资金："))
# 准备购物券
coupon = random.randint(1, 30)


# 抽取优惠券
def coupon_drawing():
    while True:
        extract = input("是否要抽取优惠券,y/n\n")
        if extract == "y":
            if coupon <= 10:
                print("恭喜你抽到一张7折老干妈优惠券!")
            else:
                print("恭喜你抽到一张联想电脑1折优惠券!")
            break
        elif extract == "n":
            print("按原价购买商品!")
            break
        else:
            print("输入错误重新输入!")


# 买东西
def shopping(extract):
    global money
    while True:
        # 展示商品
        for key, value in enumerate(shop):
            print(key, value)
        # 请输入您想要的商品
        choose = input("亲输入您想要的商品编号：")  # "1"
        # 判断是不是个数字
        if choose.isdigit():
            choose = int(choose)
            # 先判断是否存在该商品
            if choose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                if extract == "y":
                    # 5.5 判断您的余额是否足够
                    if choose == 2 and coupon > 10 and money >= shop[choose][1] * discount1:
                        # 5.6 将商品添加到购物车 ，余额减去对应的钱
                        myCart.append(shop[choose])
                        money = money - shop[choose][1] * discount1
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    elif choose == 6 and coupon <= 10 and money >= shop[choose][1] * discount2:
                        # 5.6 将商品添加到购物车 ，余额减去对应的钱
                        myCart.append(shop[choose])
                        money = money - shop[choose][1] * discount2
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    elif money > shop[choose][1]:
                        myCart.append(shop[choose])
                        money = money - shop[choose][1]
                        print("恭喜，成功添加购物车！您的余额还剩￥：", money)
                    else:
                        print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
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


# 打印城市
def print_place(choice):
    for i in choice:
        print(i)


# 攻略
for i in data:
    print(i)

while True:
    city1 = input("请输入您要去的城市：")
    if city1 in data:
        print_place(data[city1])
        city2 = input("亲输入二级城市：")
        if city2 in data[city1]:
            print_place(data[city1][city2])
            city3 = input("亲输入三级地区：")
            if city3 in data[city1][city2]:
                print_place(data[city1][city2][city3])
                while True:
                    # 是否进行购物
                    yon = input("是否要进行购买商品y/n\n")
                    if yon == "y":
                        # 商城系统
                        coupon_drawing()
                        shopping(extract="y")
                        break
                    elif yon == "n":
                        print("欢迎下次光临!")
                    else:
                        print("输入错误重新输入")
        else:
            print("当前二级城市不存在，别瞎弄！")
    elif city1 == 'q' or city1 == "Q":
        print("------------------欢迎下次光临Leo旅行社！------------------")
        break
    else:
        print("当前城市不存在，别瞎弄！")
