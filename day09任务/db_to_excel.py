
import xlwt
from DBUtils import select

n = 1
m = 0
book = xlwt.Workbook()
while True:
    if m < 12:
        sql = "select * from %s月"
        data = [int(n)]
        model = "all"
        record = select(sql, data, model, [])  # 所有数据
        sheet = book.add_sheet(str(n) + "月", m)  # 添加新的选项卡
        fields = ["日期", "服装名称", "价格/件", "库存数量", "销售量/每日"]  # 获取所有字段名
        for col, field in enumerate(fields):
            sheet.write(0, col, field)
        row = 1
        for data in record:
            for col, field in enumerate(data):
                sheet.write(row, col, field)
            row += 1
        n = n + 1
        m = m + 1

    else:
        book.save("2020年每个月的销售额.xls")
        print("插入excel表完毕!!")
        break
