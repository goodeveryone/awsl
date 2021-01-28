# 导入函数
import xlrd

# 创建一个工作簿对象f，打开文件
f = xlrd.open_workbook("python.xls")

# 获取文件中有多少工作表
# b = print(f.nsheets)

# 通过索引值方式，创建工作表对象,索引值为工作表下标
# sheet = f.sheets()[0]
# 通过工作表名称的方式i，创建工作表对象
sheet = f.sheet_by_name("sheet1")

#读取工作簿中所有的工作表
I = f.sheet_names()
# print(I)

# 读取工作表中的某一行的数据，以列表形式显示
c = sheet.row_values(0)
# print(c)

# 读取工作表中有多少行数据
d = sheet.nrows
# print(d)

# 读取工作表中的某一列的数据，以列表形式显示
e = sheet.col_values(0)
# print(e)

# 读取工作表中有多少行数据
g = sheet.ncols
# print(g)

# 获取指定单元格内的数据，(行数，列数)
f = sheet.cell(0,0).value
# print(h)

# 获取单元格内的数据类型
# 0-empty,1-string,2-number,3-date,4-booolean,5-error
ff = sheet.cell(0,0).ctype
# print(ff)
