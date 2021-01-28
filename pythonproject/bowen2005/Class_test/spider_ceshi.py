# import requests
# import re
# url = "https://www.qiushibaike.com/text/page/1/"
# head = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
# }
# r = requests.get(url,headers=head)
# # 获取请求的结果，并进行解码
# # 并不是所有的都是utf-8这种编码格式
# a = r.content.decode("utf-8")
# b = re.findall('<div class="content">(.*?)</span>',a,re.S)
# # print(b)
# with open("a.txt","a",encoding="utf8") as f:
#     for i in b:
#         c = i.replace("<span>","").replace("<br/>","").lstrip()
#         f.write(c)



import requests
import re


# class University(object):
#     def __init__(self):

url = "http://www.shanghairanking.cn/rankings/bcur/202011"
head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
}
r = requests.get(url,headers=head)
a = r.content.decode("utf-8")
# 正则表达式
b = re.findall("<tr data-v-45ac69d8><td data-v-45ac69d8>(.*?)</td></tr>",a,re.S)
# print(b)
# with open("b.txt","a",encoding="utf8") as f:
for i in b:
    c = i.replace("\n","").lstrip()
    # c = i.replace("</td><td data-v-45ac69d8>\n","").replace("</td><td data-v-45ac69d8> ","").replace("\n ","").strip()
    print(c)
# d = re.findall("<td data-v-45ac69d8>(.*?)<tr data-v-45ac69d8>",a,re.S)
# for j in b:
#     c = re.findall("<a href=(.*?) data-v-45ac69d8>",j,re.S)
#     d = re.findall("<a (.*?)</a>",j,re.S)
#     e = d[0].replace(f'href={c[0]} data-v-45ac69d8>','')
#     print(e)









