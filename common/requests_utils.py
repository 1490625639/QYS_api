# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：requests_utils.py
Author  ：张以白
Date    ：2024/3/6 23:48 
"""

import requests


class RequestUtil:
    sess = requests.session()

    # 统一请求封装
    def send_all_request(self, **kwargs):
        res=RequestUtil.sess.request(**kwargs)
        print(res.json())
        return  res

