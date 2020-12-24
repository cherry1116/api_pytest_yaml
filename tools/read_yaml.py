#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 4:41 PM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : read_yaml.py
# @Software: PyCharm


import yaml


class  DoYaml():
    def read_yaml(self,test_case_path):
        # print("*****获取yaml数据*****")
        # with open(test_case_path, encoding='utf-8')as file:
        #     content = file.read()
        #     print(content)
        #     print(type(content))
        #
        #
        #     print("\n*****转换yaml数据为字典或列表*****")
        #     # 设置Loader=yaml.FullLoader忽略YAMLLoadWarning警告
        #
        #     data = yaml.load(content, Loader=yaml.FullLoader)
            return yaml.load(open(test_case_path), Loader=yaml.FullLoader)

            # yaml.load_all(open(filename), Loader=yaml.FullLoader)






        # file=open(test_case_path)
        #
        # data=yaml.load(file)
