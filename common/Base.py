# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：Base.py
Author  ：张以白
Date    ：2024/3/9 1:19 
"""
import subprocess

from utils.log_util import my_log


def allure_report(report_path, report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 定义执行命令
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)

    my_log().info("报告地址")

    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        my_log().info("报告地址")
        raise