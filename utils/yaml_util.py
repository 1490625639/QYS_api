# -*- coding: UTF-8 -*-
"""
Project ：QYS_api 
File    ：yaml_util.py
Author  ：张以白
Date    ：2024/3/7 18:32 
"""
import os

import yaml


# 写入
def write_yaml(data):
    with open("D:/Pycharmproject/QYS_api/extract.yaml", encoding="utf8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取
def read_yaml(key):
    with open("D:/Pycharmproject/QYS_api/extract.yaml", encoding="utf8", mode="r") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[key]


# 清空
def clear_yaml():
    with open("D:/Pycharmproject/QYS_api/extract.yaml", encoding="utf8", mode="w") as f:
        f.truncate()


# 读取yaml测试用例
def read_yaml_testcase(yamlpath):
    with open("D:/Pycharmproject/QYS_api/data/" + yamlpath, encoding="utf8", mode="r") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


# 1 创建类
class YamlReader:
    # 2 初始化,文件是否存在
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileExistsError("文件不存在")
        self._data = None
        self._data_all = None

    # 3 yaml读取
    # 单个文档读取
    def data(self):

        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data = yaml.safe_load(f)
        return self._data
        # 多个文档读取

    def data_all(self):

        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all
