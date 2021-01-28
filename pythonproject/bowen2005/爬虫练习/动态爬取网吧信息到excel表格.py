import requests
import json
import xlwt
from xlutils.copy import copy
import xlrd
import time


class WangBa(object):
    def __init__(self, page):
        self.url = f'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum={page}&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=9.75&city=410000&geoobj=113.90716%7C34.517858%7C115.299169%7C35.115449&keywords=%E7%BD%91%E5%90%A7'
        self.head = {
            'Cookie': 'guid=3fc7-4a74-0d84-be64; UM_distinctid=174ba196d8b403-0ba1c5deccd8cd-333376b-144000-174ba196d8c7d6; cna=jfbxF7N+5XYCAbZ+/vh4E2ut; CNZZDATA1255626299=1376483887-1600844923-https%253A%252F%252Fditu.amap.com%252F%7C1600844923; xlly_s=1; _uab_collina=160085006460113400467047; x5sec=7b22617365727665723b32223a22316534346363613865356332363766626566373534373633393532393136663243497554725073464549615171657a55346366384d673d3d227d; isg=BCcnGDozNFVMK7DYGj1HqzUYtlvxrPuO7VZYmvmU4Lbd6EOqCX283kchCuj2BtMG; tfstk=c9NRBbADMijuSRgY78BmROMVP9gdaGL-xUip9NLZXMHk7wOets47s5H-nTge2jQA.; l=eBMP3DMnOH40Hj_pBO5Churza779VIRfGrVzaNbMiInca6aRKF_XENQ4jokyjdtjgtCflUtyNxVOSRF9-QUKOxDDBe4dDt9xWxvO.',
            'Referer': 'https://ditu.amap.com/search?query=%E7%BD%91%E5%90%A7&city=410000&geoobj=113.90716%7C34.517858%7C115.299169%7C35.115449&zoom=9.75&pagenum=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }

    def request_wangba(self):
        r = requests.get(self.url, headers=self.head)
        a = r.json()
        # print(a)
        list1 = []
        for i in range(20):
            name = a['data']['poi_list'][i]['name']
            address = a['data']['poi_list'][i]['address']
            cityname = a['data']['poi_list'][i]['cityname']
            list1.append((cityname, name, address))
        return list1

    def save_info(self):
        list2 = self.request_wangba()
        f = xlwt.Workbook(encoding='utf8')
        sheet = f.add_sheet('test')
        sheet.write(0, 0, "城市")
        sheet.write(0, 1, "名称")
        sheet.write(0, 2, "地址")
        for i, j in enumerate(list2, 1):
            for k, l in enumerate(j):
                sheet.write(i, k, l)
        f.save('bus_info.xls')

    def save_info2(self):
        list2 = self.request_wangba()
        f = xlrd.open_workbook('bus_info.xls')
        sheet = f.sheet_by_name('test')
        b = sheet.nrows
        new_f = copy(f)
        sheet1 = new_f.get_sheet(0)
        for i, j in enumerate(list2, b):
            for k, l in enumerate(j):
                sheet1.write(i, k, l)
        new_f.save('bus_info.xls')

if __name__ == '__main__':
    for i in range(1, 10):
        w1 = WangBa(i)
        if i == 1:
            w1.save_info()
        else:
            w1.save_info2()
        time.sleep(1)



