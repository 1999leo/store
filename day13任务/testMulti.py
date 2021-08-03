import unittest
from Calc import*


class TestMulti(unittest.TestCase):

    def testMulti(self):
        # 1.准备数据
        a = 6
        b = 5
        c = 30
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testMulti1(self):
        # 1.准备数据
        a = -6
        b = 5
        c = -30
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testMulti2(self):
        # 1.准备数据
        a = 6
        b = -5
        c = -30
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testMulti3(self):
        # 1.准备数据
        a = -6
        b = -5
        c = 30
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)