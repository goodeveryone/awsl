import requests
import json

def head():
    head_data={'origin': 'https://flights.ctrip.com',
               'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors',
               'sec-fetch-site': 'same-origin',
               'Accept':'*/*',
               'Accept-encoding': 'gzip, deflate, br',
               'Accept-language': 'zh-CN,zh;q=0.9',
               'Content - type': 'application/json',
               'Content-length': '287',
               'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
               'Referer': 'https://flights.ctrip.com/itinerary/oneway/hgh-bjs?date=2020-11-12',
               'Cookie':'__RF1=115.198.92.153; _RSG=fj4LbJcS8lE9OfnwrKSrX8; _RDG=288488c7b11191214c180991fa6321582e; _RGUID=ebc87264-e554-4b69-8875-714d7ac69609; MKT_CKID_LMT=1605079722397; MKT_CKID=1605079722397.ypm2b.43a1; _ga=GA1.2.1798462637.1605079722; _gid=GA1.2.392363064.1605079722; MKT_Pagesource=PC; _abtest_userid=0b5308c6-6f55-4169-8e37-dfedee9e5a81; Session=SmartLinkCode%3DU155952%26SmartLinkKeyWord%3D%26SmartLinkQuary%3D%26SmartLinkHost%3D%26SmartLinkLanguage%3D; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&createtime=1605142841&Expires=1605747641351; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index&CT=1605142841353&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={"pc_vid":"1605079719523.2xazvx"}; appFloatCnt=3; _jzqco=%7C%7C%7C%7C1605079723294%7C1.1803953149.1605079722394.1605142846062.1605142852686.1605142846062.1605142852686.undefined.0.0.15.15; __zpspc=9.4.1605142841.1605142852.4%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfa=1.1605079719523.2xazvx.1.1605087204603.1605142838474.4.26; _bfs=1.4; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D26%26v2%3D25'
               }
    url='https://flights.ctrip.com/itinerary/api/12808/products'
    request_ployed={'airportParams': [{'dcity': "hgh", 'acity': "bjs", 'dcityname': "杭州",'acityname': "北京", 'date': "2020-11-12"}],
                    'army': 'false',
                    'classType': "ALL",
                    'flightWay': "Oneway",
                    'hasBaby': 'false',
                    'hasChild': 'false',
                    'searchIndex': 1,
                    'selectedInfos': 'null',
                    'token': "bb48db28a7c8bb0abe902cde1e334c96"
                    }
    request=requests.post(url=url,data=json.dumps(request_ployed),headers=head_data)
    print(request.text)

head()
