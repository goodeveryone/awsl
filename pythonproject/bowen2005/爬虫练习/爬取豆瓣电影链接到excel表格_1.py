import re
import requests
import xlwt

url = 'https://movie.douban.com/top250?start=0&filter='
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

r = requests.get(url, headers=head)
a = r.content.decode('utf-8')
# 获取所有电影链接和名称，以一个大列表的形式显示
b = re.findall('<div class="hd">(.*?)/span>', a, re.S)
list2 = []
for i in b:
    list1 = []
    # 取出链接，以列表的形式显示
    c = re.findall('<a href="(.*?)" class="">', i ,re.S)
    # 取出电影名称，以列表的形式显示
    d = re.findall('<span class="title">(.*?)<', i, re.S)
    # 将链接和电影名称合并到新列表中
    list1.extend(c)
    list1.extend(d)
    # 将每个字列表，添加到list2大列表中
    list2.append(list1)


f = xlwt.Workbook(encoding='utf8')
sheet = f.add_sheet('test')
sheet.write(0, 0, "链接")
sheet.write(0, 1, "电影名")
for i, j in enumerate(list2, 1):
    for k, l in enumerate(j):
        print(l)
        sheet.write(i, k, l)
f.save('movie_name.xlsx')