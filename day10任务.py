"""

分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体

有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）

先构思面向对象版的中国工商银行系统

"""


# 杯子属性,功能
class Cup:
    # 属性: 高度，容积，颜色，材质
    __height = 0
    __volume = 0
    __color = ""
    __material = ""

    def setHeight(self, height):
        self.__height = height

    def setVolume(self, volume):
        self.__volume = volume

    def setColor(self, color):
        self.__color = color

    def setMaterial(self, material):
        self.__material = material

    # 功能:能存放液体
    def store(self, liquid):
        print("一个", self.__color, "的杯子,装了一杯", liquid)

    def property(self):
        print("我是一个高:", self.__height, "容积:", self.__volume, "颜色:", self.__color, "材质:", self.__material)


c = Cup()

c.setHeight(2)
c.setVolume(3)
c.setColor("黑色")
c.setMaterial("不锈钢")

c.store("雪碧")
c.property()


# 电脑属性,功能
class Computer:
    # 属性 屏幕大小，价格，cpu型号，内存大小，待机时长
    __size = ""
    __price = 0
    __model = ""
    __ram = 0
    __time = 0

    def setSize(self, size):
        self.__size = size

    def setPrice(self, price):
        self.__price = price

    def setModel(self, model):
        self.__model = model

    def setRam(self, ram):
        self.__ram = ram

    def setTime(self, time):
        self.__time = time

    # 行为（打字，打游戏，看视频）
    def tyoe(self, wordcount):
        print("我今天打了", wordcount, "个字")

    def playGames(self, game):
        print("我今天用电脑玩了", game)

    def watchVideo(self, video):
        print("我用电脑看了", video)

    def exterior(self):
        info = '''
            屏幕大小:%s
            价格:%s
            cpu型号:%s
            内存大小:%s
            待机时长 :%s      
        '''
        print(info % (self.__size, self.__price, self.__model, self.__ram, self.__time))


cp = Computer()
cp.setSize("14寸")
cp.setPrice(10000)
cp.setModel("锐龙")
cp.setRam(128)
cp.setTime(6)

cp.playGames("LoL")
cp.exterior()
