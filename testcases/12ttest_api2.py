# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：TestApi2.py
Author  ：张以白
Date    ：2024/3/7 0:21 
"""
from common.requests_utils import RequestUtil
from testcases.test_api import TestApi, timestamp


# from testcases.test_api import TestApi, timestamp
# from common.requests_utils import RequestUtil


class TestApi2:

    def test_createbycategory(self):
        print("hello导包")
        # print("hello导包测试")
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
                TestApi.documentId
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
        res = RequestUtil().send_all_request(method="post", url="http://127.0.0.1:9182//contract/createbycategory",
                                             headers=TestApi.headers, json=data)
        # res= TestApi.sess.request("post",url="http://127.0.0.1:9182//contract/createbycategory", headers=TestApi.headers, json=data)
        # res = requests.post(url="http://127.0.0.1:9182//contract/createbycategory", headers=TestApi.headers, json=data)
        TestApi.contractId = res.json()['contractId']
        # print(f"{res.json()},获取成功")

        #接口关联中，用类变量得话，会导致在执行单个用例时，由于导包的问题，会自动查找所导包的用例
        # 所以将创建合同接口分开，就是为了铭记这一点