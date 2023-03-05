#!/usr/bin/python3.8
# from urllib import response
import requests
import json
from conf import *
base_url="http://192.168.x.x"
endpoint_url="/api/v1/sms/pattern/normal/send"
sms_url = base_url + endpoint_url
final_url="http://api2.ippanel.com/api/v1/sms/pattern/normal/send"
sms_headers = {

    'Content-Type' : 'application/json',
    'apikey' : apikey
}


def send_sms(nums,name,server,dir):
    body1={
    "code": pattern_code,
    "sender": sender,
    "recipient": nums,
    "variable": {
        "user": name,
        "warning": "Disk",
        "server": server,
        "directory": dir
    }
}
    response = requests.post(url=final_url,headers=sms_headers,data=json.dumps(body1))
    f_response = json.loads(response.text)
    print("Resposns is:",response.text)


    if f_response["code"] == 200 :
        bulk_id=f_response["data"]["message_id"]
        print("bulk_id is:",bulk_id)
    else:
        err_respone=f_response["error_message"]
        print(err_respone)
