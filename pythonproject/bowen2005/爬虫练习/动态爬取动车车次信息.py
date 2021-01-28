import re
import requests
import xlwt
import xlrd
from xlutils.copy import copy

class Ticket():
    def __init__(self):
        self.url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-09-24&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT"
        self.head={
        "Cookie": "_uab_collina=160085375041677124285815; JSESSIONID=B3F5C692B829F1FCCF36B63E4B401833; BIGipServerotn=586154506.50210.0000; RAIL_EXPIRATION=1601117784455; RAIL_DEVICEID=LkXXFEZB7mP0mHxHfcqEJKFtpe5OtVNRnsu-KuP9zKKKAnESGzj_S-s8zGLqdWw9QBzLj13XcAbJ0KnGc7DED2Mootkrp-4kNSxNgErEva9PuA_B5ckb4RxnPzqO5E27rDqjyUPAMC-anaUsmU1ulJU9ILhLNNUg; BIGipServerpool_passport=283968010.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2020-09-24; _jc_save_toDate=2020-09-23; _jc_save_wfdc_flag=dc",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E4%B8%8A%E6%B5%B7,SHH&date=2020-09-24&flag=N,N,Y",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
        }
    def request_info(self):
        r = requests.get(self.url,headers=self.head)
        a = r.json()
        # print(a)
        # list1=[]
        # for i in range(len(a)):
        b = a["data"]["result"]
        # print(b)
        list1=[]
        for i in b:
            dict2={}
            d = i.split("预订")[1]
            l = d.split("|")[2:-6]
            dict2["车次"]=l[0]
            dict2["出发时间"] = l[5]
            dict2["到达时间"] = l[6]
            dict2["中途消耗"] = l[7]
            dict2["有无余票"] = l[8]
            dict2["商务座"] = l[29]
            dict2["一等座"] = l[28]
            dict2["二等座"] = l[27]
            dict2["软卧"] = l[20]
            dict2["硬卧"] = l[25]
            dict2["硬座"] = l[26]
            dict2["无座"] = l[23]
            # print(dict2)
            list1.append(dict2)
        # print(list1)
        return list1
    def save_info(self):
        list1=self.request_info()
        f = xlwt.Workbook(encoding='utf8')
        sheet = f.add_sheet('ticket')
        list4 = ["车次", "出发时间","到达时间","中途消耗","有无余票","商务座","一等座","二等座","软卧","硬卧","硬座","无座"]
        for c, d in enumerate(list4):
            # print(c)
            # print(dict1[f"{d}"])
            sheet.write(0, c, d)
        for i,j in enumerate(list1):
            # print(i)
            for x,y in enumerate(j.values()):
                sheet.write(i+1,x,y)
                # print(y)
        f.save('ticket.xls')


tickets=Ticket()
# tickets.request_info()
tickets.save_info()







