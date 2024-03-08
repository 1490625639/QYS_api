# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：conftest.py
Author  ：张以白
Date    ：2024/3/7 17:13 
"""
import time

import pytest

from common import Base
from utils.yaml_util import clear_yaml

"""@pytest.fixture(scope="function", autouse=False,params=['1','2','3'],name='cm')# [['1','2']]执行一次
def connect_mysql(request):
    print("链接数据库")
    yield   request.param       #有参数情况下写 多用于多种环境
    print("关闭数据库")"""

@pytest.fixture(scope="session", autouse=False)
# @pytest.fixture(scope="function", autouse=False)

def connect_mysql():
    clear_yaml()# 会话前清空上一次数据
    print("链接数据库")
    yield
    time.sleep(3)
    Base.allure_report('./report/result', './report/html')
    print("关闭数据库")
