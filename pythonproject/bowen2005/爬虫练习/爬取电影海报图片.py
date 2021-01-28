import re
import requests
import xlwt

url = "https://movie.douban.com/top250?qq-pf-to=pcqq.group"
head = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51"
}
# 发送请求
r = requests.get(url,headers=head)
# 解码
a = r.content.decode("utf-8")
# print(a)
b = re.findall("<li>(.*?) </li>",a,re.S)
# print(b)

list2 = []

for i in b:
    list1 = []
    c = re.findall('alt="(.*?)" src=',i,re.S)
    # print(c)
    list1.extend(c)
    d = re.findall('src="(.*?)class="">',i,re.S)
    # print(d)
    list1.extend(d)
    list2.append(list1)
print(list2)
# print(list1)


f = xlwt.Workbook(encoding='utf8')
sheet = f.add_sheet('电影介绍链接')
# 创建一个列表，用来循环插入表头
list4 = ["电影名", "超链接"]
for c, d in enumerate(list4):
    sheet.write(0, c, d)

# for m,n in enumerate(list2, 1):

for i in list2:
    # print(i)
    # i.insert()
    print(i)




# f.save('movie.xls')





















# f = xlrd.open_workbook("python.xls")
# # 复制文件并起名为new_f
# new_f = copy(f)
# # 创建一个工作表对象，用于操作整个工作表
# sheet = new_f.get_sheet(0)
# sheet.write(100, 0, "博文你好")
# new_f.save("python.xls")


























