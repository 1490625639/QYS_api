# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：AppApi.py
Author  ：张以白
Date    ：2023/11/9 1:27 
"""
import requests
import json


class AppApi:
    token = ""
    def test_token(self):
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'checkCaptcha': 'True'
        }
        data = {
            'username': '10000000001',
            'password': '{cipher}Ydk4o2z68d62uJfLJ0TzOFPpXGmUHwrWV3xO/qmgKUZuUxOoEH/USNUYHV9Xo8R0dD5ULTYt4BaAg93U6/mucFa3mqql0TKFLHFp/IhnTyNDQ8a/e7miYgfic03dPoHpZWZ3HiHnTnUE38hMr70FoyGIFrjQYt3jIGJFArH4/vs=',
        }
        response = requests.post(
            'http://127.0.0.1:9180/login', headers=headers, data=data, verify=False)
        response_text = response.content.decode('utf-8')
        res_json = json.loads(response_text)
        AppApi.token = res_json["token"]
        print(AppApi.token)
    def test_user(self):

        print(AppApi.token)
        headers={
            "X-QID":AppApi.token
        }
        res=requests.get(
            url="http://127.0.0.1:9180/user",headers=headers
        )
        response_text = res.text
        print(response_text)

    def test_user_config(self):
        print(AppApi.token)
        headers = {
            "X-QID": AppApi.token
        }
        res = requests.get(
            url="http://127.0.0.1:9180/user/get/config?", headers=headers
        )
        response_text = res.text
        print(response_text)
    def test_seal_page(self):
        print(AppApi.token)
        headers = {
            "X-QID": AppApi.token
        }
        res = requests.get(
            url="http://127.0.0.1:9180/seal/page", headers=headers
        )
        response_text = res.text
        print(response_text)
    def test_add_role(self):

        headers = {
            "Content-Length": "180",
            "Host": "127.0.0.1:9180",
            "X-QID": AppApi.token,
            "Content-Type":"application/json"

        }
        json={

                "name": "测试人员",
                "description": "22测试",
                "memberType": "ALL",
                "permissionTypes": [
                    "ORG_MANAGE"
                ],
                "orgId": "3183845632035955177"

        }
        res = requests.post(
            url="http://127.0.0.1:9180/role/add", headers=headers,json=json
        )
        response_text = res.text
        print(response_text)
if __name__ == '__main__':
    AppApi().test_token()
    # AppApi().test_user()
    # AppApi().test_user_config()
    print("------------")
    # AppApi().test_seal_page()
    AppApi().test_add_role()