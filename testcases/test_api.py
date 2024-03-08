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
from datetime import datetime

import allure
import pytest

from utils.allure_util import get_allure
from utils.log_util import my_log
from utils.yaml_util import write_yaml, read_yaml, read_yaml_testcase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import requests

from utils.requests_utils import RequestUtil

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

    """documentId = ""
    contractId = ""
    @pytest.mark.parametrize("caseinfo",["地球",'火星'])
    def test_canshu(self,caseinfo):
        print(caseinfo)
    @pytest.mark.parametrize("caseinfo2", read_yaml_testcase("test_api.yaml"))
    def test_canshu2(self, caseinfo2):
        print(caseinfo2)
        print(caseinfo2['feature'])
        print(caseinfo2['request']['method'])"""
    def test_baseurl(self, base_url,connect_mysql):  # pytest 配置base_url练习
        print(base_url)
        my_log().debug("debug测试")

    @pytest.mark.flaky(reruns=3, reruns_delay=2)    #失败重试
    @pytest.mark.parametrize("file_data", read_yaml_testcase("test_creatbyfile.yaml"))
    def test_createbyfile(self, file_data):
        file_path = file_data["file_path"]
        files = {"file": open(file_path, 'rb')}

        data = {'title': file_data["title"], 'fileType': file_data["file_type"]}
        res = RequestUtil().send_all_request(method=file_data['request']['method'], url=file_data['request']['url'],
                                             headers=TestApi.headers, files=files, data=data)
        write_yaml({
            "documentId": res.json()['result']['documentId']
        })
        print("读取", read_yaml('documentId'))
        get_allure(file_data)

    @pytest.mark.parametrize("heton", read_yaml_testcase("test_api.yaml"))
    def test_createbycategory(self, heton):
        documentId = read_yaml('documentId')
        heton['request']['json']['documents'] = [documentId]
        heton['request']['json']['subject'] += str(datetime.now())

        method = heton['request']["method"]
        url = heton['request']['url']
        res = RequestUtil().send_all_request(method=method, url=url, headers=TestApi.headers,
                                             json=heton['request']['json'])
        # # TestApi.contractId=res.json()['contractId']
        print(f"{res.json()},获取成功")
        write_yaml({
            "contractId": res.json()['contractId']
        })
        get_allure(heton)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("detail", read_yaml_testcase("test_detail.yaml"))
    def test_detail(self, detail):
        # datas = {
        #     "contractId": read_yaml('contractId')
        # }
        contractId = read_yaml('contractId')
        detail['request']['params']['contractId'] = contractId

        res = RequestUtil().send_all_request(method=detail['request']['method'], url=detail['request']['url'],
                                             headers=TestApi.headers, params=detail['request']['params'])

        response_text = res.json()
        print(response_text['contract']['subject'])
        """ # res=TestApi.sess.request("get",url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas)
        # res = requests.get(
        #     url="http://127.0.0.1:9182/contract/detail", headers=TestApi.headers, params=datas
        # )"""
        get_allure(detail)

    @pytest.mark.parametrize('signurl', read_yaml_testcase('test_signurl.yaml'))
    def test_signurl(self, signurl):
        signurl['request']['json']['contractId'] = read_yaml('contractId')

        res = RequestUtil().send_all_request(method=signurl['request']['method'], url=signurl['request']['url'],
                                             json=signurl['request']['json'],
                                             headers=TestApi.headers)

        print(res.json())
        get_allure(signurl)


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
