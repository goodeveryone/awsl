# pymysql模块负责数据库的连接与操作
import pymysql

# 连接数据库，输入四个参数：主机IP，数据库端口号，用户名，登陆密码
c = pymysql.connect(
    host="192.168.2.163",
    port=3306,
    user="root",
    passwd="111111"
)
# 创建游标
mycur=c.cursor()
# 对数据库进行操作，但是不能直接打印结果
mycur.execute("show databases;")
# 获取上一步操作的结果，进行操作（获取一条数据）
# a = mycur.fetchone()
# b = mycur.fetchone()
# 获取上一步操作的结果，进行操作（获取所有数据）
# c = mycur.fetchall()
# 获取上一步操作的结果，进行操作（小括号内输入数字几，返回几个结果）
d = mycur.fetchmany(2)
# print(a)
# print(b)
# print(c)
# print(d)
# 对数据库中的数据进行增删改的操作，先保存到缓存中，
# 当commit提交后，才会真正写入到数据库中
# mycur.execute("use bowen")
# mycur.execute("create table xxx (id char(20));")
# mycur.execute("insert into xxx values (123)")
# c.commit()


# # 将excel表格中的数据写入数据库中
# import xlrd
# f = xlrd.open_workbook("bus_info.xls")
# sheet = f.sheet_by_name("test")
# # a = sheet.row_values(1)
# # print(a)
# # print(len(sheet.nrows))
# mycur.execute("use bowen")
# mycur.execute("create table wangba (city char(20),name char(20),address char(20));")
# h = sheet.nrows
#
# for i in range(1,h):
#     a = sheet.row_values(i)
#     # print(a)
#     mycur.execute(f'insert into wangba values ("{a[0]}","{a[1]}","{a[2]}");')
# c.commit()


# 将数据库中的数据写入excel表格中
# import xlwt
# f = xlwt.Workbook(encoding="utf8")
# sheet = f.add_sheet("网吧信息")
# # 操作数据库，将读取到的 表头 添加进excel表格中
# mycur.execute("use bowen")
# mycur.execute("desc wangba;")
# a = mycur.fetchall()
# for x in range(len(a)):
#     sheet.write(0,x,a[x][0])
# # 操作数据库，将读取到的 数据 添加进excel表格中
# mycur.execute("use bowen")
# mycur.execute("select * from wangba;")
# b = mycur.fetchall()
# for i,j in enumerate(b):
#     for h,k in enumerate(j):
#         sheet.write(i+1,h,k)
# f.save("wang_ba.xls")


















