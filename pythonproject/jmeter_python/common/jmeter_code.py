
# 接口自动化测试：

# 手机自动化测试框架：
# python+appium+unittest+HtmlTestRunner+yaml+log

# 接口自动化测试框架：requests 模块 发送请求
# python+requests+unittest+HtmlTestRunner+yaml+log

# common  config  date test_case  tese_run  report



import requests
import json
import csv

def duqu_csv():
    csvshuju=[]
    with open('../date/aaa.csv','r',encoding='utf-8') as f:
        read = csv.reader(f)
        for line in read:
            # print(line)
            csvshuju.append(line)
        # print(csvshuju)
    return csvshuju

class Movie(object):
    def __init__(self):
        self.header={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58'
        }
    def find(self,tit,key,num):
        url='http://v.juhe.cn/movie/index'
        date=f'title={tit}&key={key}&smode={num}'
        # get请求时参数传递给 params
        # post请求时参数传递给 data,参数有中文时要先编码
        res=requests.get(url,headers=self.header,params=date)
        print(res.url)
        return res.json()

if __name__ == "__main__":
    movie=Movie()
    movie.find('哥斯拉','0bc5d7de815a4585fa9e5aebdf807666','1')

