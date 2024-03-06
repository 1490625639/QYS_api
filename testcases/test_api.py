# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：test_api.py
Author  ：张以白
Date    ：2024/3/6 15:05 
"""
import hashlib
import time
import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import requests

from common.requests_utils import RequestUtil

timestamp = str(int(time.time() * 1000))


class TestApi:
    AppToken = "NkX7veUo25"
    AppSecret = "L4PHgt2JPscm2ycfxTb8GxBDyO5Z3D"
    timestamp = str(int(time.time() * 1000))  # 获取当前时间戳并转换为字符串形式
    signature = AppToken + AppSecret + timestamp
    md5_hash = hashlib.md5(signature.encode()).hexdigest()  # 计算MD5哈希值
    sess = requests.session()
    URL = "http://127.0.0.1:9182/"

    headers = {
        "x-qys-accesstoken": AppToken,
        "x-qys-timestamp": timestamp,
        "x-qys-signature": md5_hash

    }
    documentId = ""
    contractId = ""
    @pytest.mark.file

    def test_createbyfile(self):
        file_path = "D:/Desktop/面试/20220613面试复盘.docx"  # 替换为你要上传的文件路径
        files = {"file": open(file_path, 'rb')}
        data = {'title': 'YourTitle', 'fileType': 'docx'}  # 其他参数
        res=RequestUtil().send_all_request(method="post", url="http://127.0.0.1:9182/v2/document/createbyfile", headers=TestApi.headers, files=files, data=data)
        # res= TestApi.sess.request("post", url="http://127.0.0.1:9182/v2/document/createbyfile", headers=TestApi.headers, files=files, data=data)
        # res = requests.post(
        #     url="http://127.0.0.1:9182/v2/document/createbyfile", headers=TestApi.headers, files=files, data=data
        # )
        TestApi.documentId = res.json()['result']['documentId']

    @pytest.mark.smoke
    def test_detail(self):
        datas = {
            "contractId": "3202893801130754238"
        }
        res = RequestUtil().send_all_request(method="get",url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas)
        # res=TestApi.sess.request("get",url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas)
        # res = requests.get(
        #     url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas
        # )
        response_text = res.json()
        # print(response_text)

    # def test_createbycategory(self):
    #     data = {
    #
    #         "subject": f"open-企业{timestamp}",
    #         "description": "描述",
    #         "sn": "",
    #         "ordinal": True,
    #         "categoryId": "3183852085512216651",
    #         "creatorName": "张豪",
    #         "creatorContact": "10000000001",
    #         "tenantName": "众畅科技",
    #         "endTime": "",
    #         "documents": [
    #             TestApi.documentId
    #         ],
    #         "signatories": [
    #             {
    #                 "tenantType": "COMPANY",
    #                 "tenantName": "众畅科技",
    #                 "receiverName": "张豪",
    #                 "contact": "10000000001",
    #                 "serialNo": 1,
    #
    #                 "actions": [
    #                     {
    #                         "type": "PERSONAL",
    #                         "name": "个人签字",
    #                         "serialNo": 1,
    #                         "actionOperators": [
    #                             {
    #                                 "operatorContact": "10000000001"
    #                             }
    #                         ]
    #                     }
    #                 ]
    #             },
    #             {
    #                 "tenantType": "PERSONAL",
    #                 "tenantName": "张豪",
    #                 "contact": "10000000001",
    #                 "serialNo": 1,
    #                 "remind": True,
    #                 "actions": [
    #                     {
    #                         "type": "PERSONAL",
    #                         "name": "个人签字",
    #                         "serialNo": 1,
    #                         "addEmployee": True,
    #                         "canNotify": False,
    #                         "canModify": False,
    #                         "complete": False
    #                     }
    #                 ]
    #             }
    #         ]
    #
    #     }
    #     res = RequestUtil().send_all_request(method="post",url="http://127.0.0.1:9182//contract/createbycategory", headers=TestApi.headers, json=data)
    #     # res= TestApi.sess.request("post",url="http://127.0.0.1:9182//contract/createbycategory", headers=TestApi.headers, json=data)
    #     # res = requests.post(url="http://127.0.0.1:9182//contract/createbycategory", headers=TestApi.headers, json=data)
    #     TestApi.contractId=res.json()['contractId']
    #     # print(f"{res.json()},获取成功")

    def test_signurl(self):
        data = {
            "contractId": TestApi.contractId,
            "tenantName": "张豪",
            "tenantType": "PERSONAL",
            "contact": "10000000001",
            "canLpSign": "1",
            "language": "ZH_CN",
            "canReturn": False,
            "canWithdraw": False,
            "canViewDetail": False}
        res = RequestUtil().send_all_request(method="post",url="http://127.0.0.1:9182/contract/signurl",json=data,headers=TestApi.headers)
        # res=TestApi.sess.request("post",url="http://127.0.0.1:9182/contract/signurl",json=data,headers=TestApi.headers)
        # res = requests.post(url="http://127.0.0.1:9182/contract/signurl",json=data,headers=TestApi.headers)
        # print(res.json())

if __name__ == '__main__':
    TestApi().test_detail()
    TestApi().test_createbyfile()
    # TestApi2().test_createbycategory()
    TestApi().test_signurl()
