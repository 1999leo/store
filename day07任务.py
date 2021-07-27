"""
    任务：
    每个月的销售总金额：
    全年的销售总额：
    每种衣服的销售总额：
    每个季度销售总额占比：
    全年每种销售数量占比：
"""
import xlrd

wd = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx", encoding_override=True)

# 选项卡列表
m = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

# 衣服列表
clothes = ['羽绒服', '牛仔裤', '风衣', '皮草', 'T血', '马甲', '小西装', '皮衣', '衬衫', '休闲裤', '卫衣', '棉衣', '铅笔裤']

# 全年销售总额初始化
all_count = 0

# 每月销售总额列表
tms = []

# 每种衣服的销售量列表
ct = []

# 衣服销售总量初始化
ts = 0

# 每季度销售额列表
quarterly = [1, 2, 3, 4]


# 每月销售金额
def per_month(month):
    st = wd.sheet_by_name(month)  # 读取选项卡
    rows = st.nrows  # 获取所有行
    sum_total = 0  # 每个月销售总金额初始化
    for i in range(1, rows):
        cell = st.row_values(i)
        sum_total = sum_total + (cell[2] * cell[4])  # 每月销售总额
    return sum_total


# 每种衣服的销售总额计算逻辑
def clothes_typeof(type):
    sales_amount = 0  # 销售金额
    sales = 0  # 销量
    for month in m:
        st = wd.sheet_by_name(month)  # 读取选项卡
        rows = st.nrows  # 获取行数
        for i in range(1, rows):
            cell = st.row_values(i)
            if type == cell[1]:
                sales_amount = cell[2] * cell[4] + sales_amount
                sales = sales + cell[4]
    return sales_amount, sales


# 每月的销售总额
print("每月的销售总额".center(25, "-"))
for month in m:
    money = per_month(month)
    tms.append(money)
    print(month, "的月销售总额", round(money, 1), "元")
    all_count = all_count + money  # 全年的销售总额计算
print("-".center(30, "-"))
print("全年销售总额为", round(all_count, 2))

# 每种衣服的销售总额
print("每种服装的销售总额".center(25, "-"))
for t in clothes:
    data = clothes_typeof(t)
    print(t, "的销售总额额为：", round(data[0]), "元")
    ts = ts + data[1]
    ct.append(data[1])

# 每季度销售额占比
print("每个季度销售总额占比".center(25, "-"))
for key, value in enumerate(tms):
    if 0 <= key < 3:  # 第一季度
        quarterly[0] += value
    elif 3 <= key < 6:  # 第二季度
        quarterly[1] += value
    elif 6 <= key < 9:  # 第三季度
        quarterly[2] += value
    else:  # 第四季度
        quarterly[3] += value
for key, value in enumerate(quarterly):
    print("第", key + 1, "季度销售额占比为：", round((value / all_count) * 100, 2), "%")

# 每种衣服的销量占比
print("每种衣服的销量占比".center(25, "-"))
for key, value in enumerate(clothes):
    print(value, "的销售量占比为", round((100 * ct[key]) / ts, 2), "%")

    
