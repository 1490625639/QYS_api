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

from common.yaml_util import write_yaml, read_yaml, read_yaml_testcase

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
    # documentId = ""
    # contractId = ""
    # @pytest.mark.parametrize("caseinfo",["地球",'火星'])
    # def test_canshu(self,caseinfo):
    #     print(caseinfo)

    @pytest.mark.parametrize("caseinfo2", read_yaml_testcase("test_api.yaml"))
    def test_canshu2(self, caseinfo2):
        print(caseinfo2)
        print(caseinfo2['feature'])
        print(caseinfo2['request']['method'])
    def test_baseurl(self,base_url):#pytest 配置base_url练习
        print(base_url)

    # @pytest.mark.file
    # def test_createbyfile(self, cm):
        # print("fixture别名",cm)
    def test_createbyfile(self,connect_mysql):
        file_path = "D:/Desktop/面试/20220613面试复盘.docx"  # 替换为你要上传的文件路径
        files = {"file": open(file_path, 'rb')}
        data = {'title': 'YourTitle', 'fileType': 'docx'}  # 其他参数
        res = RequestUtil().send_all_request(method="post", url="http://127.0.0.1:9182/v2/document/createbyfile",
                                             headers=TestApi.headers, files=files, data=data)
        # res= TestApi.sess.request("post", url="http://127.0.0.1:9182/v2/document/createbyfile", headers=TestApi.headers, files=files, data=data)
        # res = requests.post(
        #     url="http://127.0.0.1:9182/v2/document/createbyfile", headers=TestApi.headers, files=files, data=data
        # )
        write_yaml({
            "documentId":res.json()['result']['documentId']
        })
        print("读取",read_yaml('documentId'))
        # TestApi.documentId = res.json()['result']['documentId']
        # print(res.json()["result"])


    @pytest.mark.parametrize("heton", read_yaml_testcase("test_api.yaml"))
    def test_createbycategory(self,heton):
        data = {

            "subject": f"open-企业{timestamp}",
            "description": "描述",
            "sn": "",
            "ordinal": True,
            "categoryId": "3183852085512216651",
            "creatorName": "张豪",
            "creatorContact": "10000000001",
            "tenantName": "众畅科技",
            "endTime": "",
            "documents": [
                # TestApi.documentId
                read_yaml('documentId')
            ],
            "signatories": [
                {
                    "tenantType": "COMPANY",
                    "tenantName": "众畅科技",
                    "receiverName": "张豪",
                    "contact": "10000000001",
                    "serialNo": 1,

                    "actions": [
                        {
                            "type": "PERSONAL",
                            "name": "个人签字",
                            "serialNo": 1,
                            "actionOperators": [
                                {
                                    "operatorContact": "10000000001"
                                }
                            ]
                        }
                    ]
                },
                {
                    "tenantType": "PERSONAL",
                    "tenantName": "张豪",
                    "contact": "10000000001",
                    "serialNo": 1,
                    "remind": True,
                    "actions": [
                        {
                            "type": "PERSONAL",
                            "name": "个人签字",
                            "serialNo": 1,
                            "addEmployee": True,
                            "canNotify": False,
                            "canModify": False,
                            "complete": False
                        }
                    ]
                }
            ]

        }
        method=heton['request']["method"]
        url=heton['request']['url']
        res = RequestUtil().send_all_request(method=method,url=url, headers=TestApi.headers, json=data)
        # TestApi.contractId=res.json()['contractId']
        print(f"{res.json()},获取成功")

        write_yaml({
            "contractId":res.json()['contractId']
        })

    # @pytest.mark.smoke
    def test_detail(self, base_url):
        datas = {
            "contractId": read_yaml('contractId')
        }
        url = base_url + "/contract/detail"
        res = RequestUtil().send_all_request(method="get", url=url, headers=TestApi.headers, params=datas)
        # res=TestApi.sess.request("get",url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas)
        # res = requests.get(
        #     url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas
        # )
        response_text = res.json()
        print(response_text['contract']['subject'])
    def test_signurl(self):
        data = {
            "contractId": read_yaml('contractId'),
            "tenantName": "张豪",
            "tenantType": "PERSONAL",
            "contact": "10000000001",
            "canLpSign": "1",
            "language": "ZH_CN",
            "canReturn": False,
            "canWithdraw": False,
            "canViewDetail": False}
        res = RequestUtil().send_all_request(method="post", url="http://127.0.0.1:9182/contract/signurl", json=data,
                                             headers=TestApi.headers)

        print(res.json())


if __name__ == '__main__':
    TestApi().test_detail()
    TestApi().test_createbyfile()
    # TestApi2().test_createbycategory()
    TestApi().test_signurl()


""" # def setup_method(self):
    #     print("用例执行前操作")
    # def teardown_method(self):
    #     print("用例结束后执行")
    # def setup_class(self):
    #     print("每个类执行前操作")
    # def teardown_class(self):
    #     print("每个类执行后操作")"""