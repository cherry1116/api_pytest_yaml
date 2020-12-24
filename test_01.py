#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 4:39 PM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : test_01.py
# @Software: PyCharm

import os
import pytest
import allure

import jsonpath

from tools.read_yaml import DoYaml
from tools.project_path import *
from tools.http_request import HttpRequest
from tools.assert_response import AssertResponse
from tools.get_token import GetToken
from tools.get_baseUrl import GetBaseUrl

test_data=DoYaml().read_yaml(test_zhibo_path)
# print(test_data)

class Test:
    def setup(self):
        pass

    def teardown(self):
        pass


    @allure.feature('test_api')
    @pytest.mark.parametrize("item",test_data)
    def test_01(self,item):
        data_list=item["test"]
        print(data_list)
        request_data=data_list.get('request')
        url=GetBaseUrl().get_baseUrl()+request_data.get('url')
        method=request_data.get('method')
        data_json=request_data.get('json')
        token=GetToken().get_token()
        if url.find("$")==-1:
            response=HttpRequest().http_request(url,data_json,method,token)
        # 判断是否有extract提取参数
        if data_list.get("extract"):
            for key, value in data_list.get("extract").items():
                os.environ[key]= jsonpath.jsonpath(response.json(), value)[0]
        if url.find("$liveRoomId")>0 or str(data_json).find("$liveRoomId")>0 :
            if url.find("$liveRoomId")>0:
                url=url.replace("$liveRoomId" , os.environ['liveRoomId'])
            if str(data_json).find("$liveRoomId")>0 :
                data_json=str(data_json).replace("$liveRoomId",os.environ['liveRoomId'])
            response=HttpRequest().http_request(url,data_json,method,token)
        validate=data_list.get("validate")
        AssertResponse().assert_response(response,validate)


if __name__ == '__main__':
    #多进程 多线程

    import pytest
    pytest.main(['-s','-q','test_01.py','--workers=2','--test-per-worker=2','--alluredir','./Outputs/Reports'])

