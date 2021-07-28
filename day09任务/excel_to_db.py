import xlrd

from DBUtils import *

n = 0
wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx", encoding_override=True)  # 打开excel
create()
while True:
    if n < 12:
        sheet = wd.sheet_by_index(n)
        rows = sheet.nrows  # 所有行
        for i in range(1, rows):
            date = sheet.cell_value(i, 0)  # 获取日期
            name = sheet.cell_value(i, 1)  # 获取服装的名称
            price = float(sheet.cell_value(i, 2))  # 获取单价
            count = int(sheet.cell_value(i, 3))  # 获取库存量
            sales = int(sheet.cell_value(i, 4))  # 获取日销售量
            sql = "insert into %s月 values (%s,%s,%s,%s,%s)"
            data = [int(n + 1), date, name, price, count, sales]
            update(sql, data)
        n = n + 1
    else:
        print("插入数据库完成!!")
        break
