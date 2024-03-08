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

from common import Base
from utils.yaml_util import write_yaml, read_yaml, clear_yaml, read_yaml_testcase

if __name__ == '__main__':

    pytest.main()
    time.sleep(3)
    Base.allure_report('./report/result','./report/html')

# write_yaml(data={"name":"张彤123"})


    # print(read_yaml_testcase("test_api.yaml"))
