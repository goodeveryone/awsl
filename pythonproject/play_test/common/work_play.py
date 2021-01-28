import requests
import csv
import json

def duqu_csv():
    csvshuju = []
    with open('',encoding='utf_8') as f:
        read = csv.reader(f)
        for i in read:
            csvshuju.append(i)
    return csvshuju

class movie(object):
    def __init__(self):
        self.header={
            '':''
        }

    def find(self,tit,key,num):
        url = ''
        data = f''
        res = requests.get(url,header = self.header,params = data)
        print(res.url)
        return res.json()


if __name__ == '__main__':
    Movie = movie()
    movie.find()
