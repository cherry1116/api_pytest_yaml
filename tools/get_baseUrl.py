#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 3:09 PM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : get_baseUrl.py
# @Software: PyCharm

from tools.read_yaml import DoYaml
from tools.project_path import *

class GetBaseUrl:
    def get_baseUrl(self):
        data=DoYaml().read_yaml(env_path)
        data_list=data[0]["test"]
        if data_list.get("name")=="测试环境":
            base_url=data_list.get("url")
            return base_url