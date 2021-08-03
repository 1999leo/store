import unittest
from Calc import*


class TestDivision(unittest.TestCase):

    def testDivision(self):
        # 1.准备数据
        a = 6
        b = 6
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.division(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testDivision1(self):
        # 1.准备数据
        a = -6
        b = -6
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.division(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testDivision2(self):
        # 1.准备数据
        a = 6
        b = -6
        c = -1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.division(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testDivision3(self):
        # 1.准备数据
        a = -6
        b = 6
        c = -1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.division(a, b)

        # 3.断言
        self.assertEqual(c, sum)