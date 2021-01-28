

import re
import requests
import xlwt

for i in range(10):
    url = f'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum={i}&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=9.75&city=410000&geoobj=113.90716%7C34.517858%7C115.299169%7C35.115449&keywords=%E7%BD%91%E5%90%A7'
    head = {
    'Cookie': 'guid=b0c4-e02d-b3db-9e81; UM_distinctid=174b9e3d43aef-08bddb7ac50717-333376b-144000-174b9e3d43bc6; cna=1OjxF4i/nAYCAbZ+/vj8zgdN; CNZZDATA1255626299=992710216-1600844923-https%253A%252F%252Fditu.amap.com%252F%7C1600844923; xlly_s=1; _uab_collina=160084655205596397560605; x5sec=7b22617365727665723b32223a226263616161353163353333616461656639653331653432616432303365616462434c2f32712f73464550794a7771664e33386e6a7567453d227d; isg=BA8PVqKpjGwW3IiQ4rXv440gnqMZNGNWRV5A0iEcVX6F8C_yKwYRpvgp8iDOjjvO; l=eBMP3DMnOH40HDKOBO5Courza77OXIRb4rVzaNbMiInca6NP1FKzWNQ4btt6Rdtjgt1vsexyNxVOSRLHR3cK9xDDBy7i_23Enxf..; tfstk=cXBlBbirJ_R5PpAc1895fufAH14OZUPyP9WV3t4EK7a1_w6Vitcq_reLmUQlpX1..',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Referer":"https://ditu.amap.com/search?query=%E7%BD%91%E5%90%A7&city=410000&geoobj=114.109734%7C34.538299%7C115.175993%7C35.101239&zoom=9.54",
    "Host": "ditu.amap.com",
    }
    r = requests.get(url, headers=head)
    a = r.json()

    # print(a)
    list2 = []
    for p in range(len(a["data"]["poi_list"])):
        # print(i)
        list1 = []
        b = a["data"]["poi_list"][p]["disp_name"]
        c = a["data"]["poi_list"][p]["address"]
        list1.append((b,c))
        # list1.append(c)
        list2.extend(list1)
    print(list2)
    # list3=[]
    # list3.extend(list2)
    # print(list3)
def save_info1():
    f = xlwt.Workbook()
    sheet = f.add_sheet("网吧信息")
    list4 = ["网吧名字", "网吧位置"]
    for c, d in enumerate(list4):
        sheet.write(0, c, d)
    for g,h in enumerate(list2,1):
        for x,y in enumerate(h):
            # print(y)
            sheet.write(g,x,y)
    f.save("wanba_info.xls")

# def save_info2():




























