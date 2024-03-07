# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：yaml_util.py
Author  ：张以白
Date    ：2024/3/7 18:32 
"""
import os

import yaml

#写入
def write_yaml(data):
    with open("D:/Pycharmproject/QYS_api/extract.yaml",encoding="utf8",mode="a+") as  f:
        yaml.dump(data, stream=f ,allow_unicode=True )
#读取
def read_yaml(key):
    with open("D:/Pycharmproject/QYS_api/extract.yaml",encoding="utf8",mode="r") as  f:
        value=yaml.load(f,Loader=yaml.FullLoader)
        return value[key]

# 清空
def  clear_yaml():
    with open("D:/Pycharmproject/QYS_api/extract.yaml",encoding="utf8",mode="w") as  f:
        f.truncate()

# 读取yaml测试用例
def read_yaml_testcase(yamlpath):
    with open("D:/Pycharmproject/QYS_api/testcases/"+yamlpath,encoding="utf8",mode="r") as  f:
        value=yaml.load(f,Loader=yaml.FullLoader)
        return value