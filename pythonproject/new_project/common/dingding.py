import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=36bb5f2e313b5565d477e9806c2556a63c87882a18760fd5d30436cecdef2dee'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('我，你的测试报告已完成，请签收')
        },
        "at":{
            "atMobiles":[
                "15188385283"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True   #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()
