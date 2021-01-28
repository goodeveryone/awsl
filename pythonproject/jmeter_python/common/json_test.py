# import json
# a={'a':123,'b':456}
#
# # json.dumps：将字典格式数据转换为json格式
# b=json.dumps(a)
# print(b)
# print(type(b))
#
# # json.loads：将json格式数据转换为字典格式
# c=json.loads(b)
# print(c)
# print(type(c))

# str1='aabbcc'
# dict1={}
# for i in str1:
#     dict1[i] = str1.count(i)
# print(dict1)

import csv
with open('../date/aaa.csv','rb') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i['turnoverVol'])




