#导入xlutils包下面的copy模块下的copy方法
from xlutils.copy import copy
import xlrd

f = xlrd.open_workbook("python.xls")

#复制文件并起名为new_f
new_f = copy(f)

# 创建一个工作表对象，用于操作整个工作表
sheet = new_f.get_sheet(0)
sheet.write(100,0,"博文你好")

new_f.save("python.xls")



import time
# # 时间戳
# print(time.time())
# # 结构化时间——本地时区（东八区）
# print(time.localtime())
# # 结构化时间——utc时区
# print(time.gmtime())

# 时间格式相互转换
# 结构化时间—→格式化时间
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 格式化时间—→结构化时间
# print(time.strptime("2020-09-21 15:47:26","%Y-%m-%d %H:%M:%S"))

# print(time.mktime(time.localtime()))


































