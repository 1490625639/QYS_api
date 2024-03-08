# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：allure_util.py
Author  ：张以白
Date    ：2024/3/9 1:58 
"""
import allure


# allure
def get_allure(data):
    allure.dynamic.feature(data['feature']) # 一级标签
    allure.dynamic.story(data['story'])  # 二级标签:模块
    # allure.dynamic.title(case_id + case_name)  # 标题
    allure.dynamic.title(data['title'])
    # desc = \
    # "<font color='red'>请求URL:    </font> {} <Br/>" \
    # "<font color='red'>请求类型:        </font> {} <Br/>" \
    # .format(data['request']['url'], data['request']['method'])  # 格式化转成字符串并添加网页标签
    # allure.dynamic.description(desc)  # 描述