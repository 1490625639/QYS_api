# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：run.py
Author  ：张以白
Date    ：2024/3/7 1:26 
"""
import time

import pytest
import os

import config.config
from common import Base
from utils.yaml_util import write_yaml, read_yaml, clear_yaml, read_yaml_testcase

if __name__ == '__main__':

    # pytest.main()
    # time.sleep(3)
    # Base.allure_report('./report/result','./report/html')
    report_path=config.config.get_report_path()+os.sep+"result"
    report_html_path=report_path+os.sep+"html"
    Base.send_mail(content=report_html_path,title='我的测试报告')
    # write_yaml(data={"name":"张彤123"})
    # print(read_yaml_testcase("test_api.yaml"))
