# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：login.py
Author  ：张以白
Date    ：2023/11/9 1:27 
"""
import requests
import json
class Login():
    cookies = {
    }
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'checkCaptcha':'True'
    }

    params = {
    }

    data = {
        'username': '10000000001',
        'password': 'qiyuesuo#2020',
    }
    def test_login(self):
        response = requests.post(
            'http://app95.qiyuesuo.net/api/login',
            params=self.params, cookies=self.cookies, headers=self.headers, data=self.data, verify=False)

        # 获取响应信息
        response_text = response.content.decode('utf-8')
        print(response_text)
        # 获取结果转字典
        res_json = json.loads(response_text)
        print(f"响应转字典：{res_json}")
if __name__ == '__main__':
    res=Login().test_login()
