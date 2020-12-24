#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 3:09 PM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : get_token.py
# @Software: PyCharm

import requests
from tools.read_yaml import DoYaml
from tools.project_path import *

class GetToken:
    def get_token(self):
        data=DoYaml().read_yaml(test_login_path)
        data_list=data[0]["test"]
        request_data=data_list.get('request')
        url=request_data.get('url')
        method=request_data.get('method')
        data_json=request_data.get('json')
        header={"Content-Type":"application/json"}
        if method=='POST':
            response=requests.post(url,json=data_json,verify=False,headers=header)
            token=response.json().get('token')
            return token