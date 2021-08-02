"""
按要求定义类
考查知识点：super关键字的使用和继承中方法的调用
要求：
1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”要求打印“正在给xxx打电话...”
   这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
4、使用新手机对象调用手机介绍的方法；
5、使用新手机对象调用打电话的方法；

"""
import time


class OldPhone:
    def __init__(self, brand):
        self.__brand = brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def call(self, phoneNumber):
        print("正在给{}打电话".format(phoneNumber))


class NewPhone(OldPhone):
    def call(self, phoneNumber):
        print("语音拨号中...", end="")
        for i in range(5):
            print(".", end="")
            time.sleep(1)
        super().call(phoneNumber)

    def show(self):
        print("品牌为：{}的手机很好用...".format(super().get_brand()))


class TestOne:
    p= NewPhone("Apple")
    p.set_brand("华为")
    p.show()
    p.call("11111111")
    print("-".center(30,"-"))


"""

要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；

"""


class Chef:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def steam_rice(self):
        print("正在蒸饭...")


class Son(Chef):
    def cook(self):
        print("正在炒菜...")


class Grandson(Son):
    def steamedRice(self):
        print("蒸饭")

    def cook(self):
        print("炒菜")


class TestTwo:
    t = Grandson("夏云鹏", 22)
    name = t.get_name()
    age = t.get_age()
    print("我叫{}， 今年{}岁".format(name, age))
    t.cook()
    t.steamedRice()
    print("-".center(30,"-"))


"""

请编程
i.	人：年龄，性别，姓名。

ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

"""


class Person:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def getAge(self):
        return self.__age


class Worker(Person):
    def work(self):
        print("我是工人，我叫{}，性别{}，今年{}岁，正在工作中...".format(
            super().getName(),
            super().getSex(),
            super().getAge())
        )


class Student(Person):
    def __init__(self, name, sex, age, id):
        super().__init__(name, sex, age)
        self.__id = id

    def study(self):
        print("我是学生中，我叫{}，性别{}，今年{}岁，学号是{}, 正在学习中...".format(
            super().getName(),
            super().getSex(),
            super().getAge(),
            self.__id)
        )


class TestThree:
    w = Worker("张三", "男", 22)
    w.work()
    s = Student("李四", "男", 33, "12321313")
    s.study()
