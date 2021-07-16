'''
    猜数字游戏：
        需求：
            1.系统产生一个随机数，
            2.用户从键盘输入数据，与随机数进行比对
                2.1 若大了，温馨提示：大了
                2.2 若小了，提示：小了
                2.3 提示：恭喜您，猜中！
    任务：
        加上金币赌博功能。
            初始化有2000金币，没猜错一次，扣200金币。
            10机会，钱扣完为止。
            在机会过程中，若猜中，奖励5000金币。
            然后询问，是否继续？是，否。
'''
import random

# 1. 让系统产生一个随机数
data = random.randint(0, 10)  # 22
# 初始化次数
count = 0
# 初始化金币 20001

gold = 2000

while True:
    try:
        if gold == 0 or count == 10:
            print("金币不足/次数用尽，强制退出游戏")
            break

        else:
            count += 1
            num = input("请输入您要猜的数字：")
            num = int(num)

            if num > data:
                gold -= 200
                print("大了！所剩金币:", gold)
            elif num < data:
                gold -= 200
                1
                print("小了！所剩金币:", gold)
            else:
                gold -= 200
                gold += 5000
                print("恭喜，猜中了！本次幸运数字为：", data, "，本次猜了", count, "次！", "所剩金币为:", gold)
                yon = input("是否继续游戏（y/n）：")
                if yon == "n":
                    print("ByeBye!")
                    break
                elif yon == "y":
                    count = 0  # 次数重置
                    data = random.randint(1, 10)  # 重新获取随机数
                else:
                    print("输入错误退出游戏!")
                    break
    except:
        print("输入非法重新输入!")
        pass
