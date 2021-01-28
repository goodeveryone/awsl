import re
import requests
import xlwt

url = f'http://book.zongheng.com/api/chapter/chapterinfo?bookId=892247&chapterId=58415938&_=1601187613092'
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'
            }

r = requests.get(url, headers=head)
a = r.content.decode('utf-8')
# print(a)

list1=[]
b = re.findall('"chapterName":"(.*?)","wordNum"', a, re.S)
c = re.findall('"content":"(.*?)","tomeId":', a, re.S)
d = c[0].replace("<p>","").replace("</p><p>","").replace("</p>","\n")
# print(d)6
list1.append((b[0],d))
# print(type(list1[0][1]))
# x=requests.get(list1[0][1])
# y = x.content
f = open(fr'D:\PythonProject\bowen2005\Novel小说\{list1[0][0]}.txt','a')
f.write(list1[0][1])
f.close()




# for k in list1:
#     print(k)
#     # 网址循环遍历
#     x=requests.get(k[1])
#     # print(k[1])
#     # 字节类型的二进制
#     y = x.content
#     # 保存图片
#     f = open(fr'D:\PythonProject\bowen2005\Novel小说\{k[0]}.txt','wb')
#     f.write(y)
#     f.close()


