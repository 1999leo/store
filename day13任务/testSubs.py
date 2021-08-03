import unittest
from Calc import*


class TestSubs(unittest.TestCase):

    def testSubs(self):
        # 1.准备数据
        a = 6
        b = 5
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testSubs1(self):
        # 1.准备数据
        a = -6
        b = -5
        c = -1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testSubs2(self):
        # 1.准备数据
        a = -6
        b = 5
        c = -11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testSubs3(self):
        # 1.准备数据
        a = 6
        b = -5
        c = 11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)