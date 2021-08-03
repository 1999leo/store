import threading
from threading import Thread
import time

# 初始化
bread = 600


# 厨师
class Chef(Thread):
    username = ""
    # mutex1 = threading.Lock()

    def run(self) -> None:
        global bread
        while True:
            # self.mutex1.acquire()
            if bread < 600:
                # time.sleep(0.5)
                bread += 1
                print("篮子里总共有{}个面包".format(bread))
            elif bread == 600:
                time.sleep(0.5)
                print("篮子满了")
            # self.mutex1.release()


# 顾客
class Client(Thread):
    username = ""
    money = 3000
    count = 0
    # mutex = threading.Lock()

    def run(self) -> None:
        global bread
        while True:
            # self.mutex.acquire()
            if self.money > 2:
                if bread > 0:
                    bread -= 1
                    self.money -= 2
                    self.count += 1
                    print("顾客{}已买了{}个面包".format(self.username, self.count))
                else:
                    print("没面包了")
                    time.sleep(1)
            else:
                print("顾客{}已消费完".format(self.username))
                break
            # self.mutex.release()


c1 = Chef()
c2 = Chef()
c3 = Chef()

p1 = Client()
p2 = Client()
p3 = Client()
p4 = Client()
p5 = Client()
p6 = Client()

c1.username = "厨师1"
c2.username = "厨师2"
c3.username = "厨师3"

p1.username = "张三"
p2.username = "李四"
p3.username = "王五"
p4.username = "赵六"
p5.username = "吴七"
p6.username = "周八"

c1.start()
c2.start()
c3.start()

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
