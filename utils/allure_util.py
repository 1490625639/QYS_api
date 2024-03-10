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
