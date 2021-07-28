import pymysql

host = 'localhost'
user = 'root'
password = 'root'
database = 'shopping'


# 创建表
def create():
    for a in range(1, 13):
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cur = con.cursor()
        sql = "CREATE TABLE %s月 (" \
              "`date` VARCHAR(10)," \
              "`name` VARCHAR(10)," \
              "`price` DOUBLE(11,2)," \
              "`count` INT(11)," \
              "`sales` INT(11) " \
              ") CHARSET=utf8;"
        data = [int(a)]
        cur.execute(sql, data)
        con.commit()
        cur.close()
        con.close()


# 改
def update(sql, data):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# 查
def select(sql, data, model, size):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, data)
    if model == "all":
        return cur.fetchall()
    elif model == "one":
        return cur.fetchone()
    elif model == "many":
        return cur.fetchmany(size)
    con.commit()
    cur.close()
    con.close()
