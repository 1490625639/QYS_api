# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：Base.py
Author  ：张以白
Date    ：2024/3/9 1:19 
"""
import subprocess

from utils.EmailUtil import SendEmail
from utils.log_util import my_log
from config.config import ConfigYaml


def allure_report(report_path, report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 定义执行命令
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)

    # my_log().info("报告地址")

    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        my_log().info("报告地址")
        raise


def send_mail(report_html_path="",content="",title="测试报告"):
    """
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()
