#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 10:20 AM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : assert_response.py
# @Software: PyCharm

import jsonpath

class AssertResponse:
    def assert_response(self, response, validate):
        '''设置断言'''

        if validate:
            for i in validate:
                if "eq" in i.keys():
                    yaml_result = i.get("eq")[0]
                    actual_result = jsonpath.jsonpath(response.json(), yaml_result)
                    expect_result = i.get("eq")[1]
                    print("实际结果：%s" % actual_result[0])
                    print("期望结果：%s" % expect_result)
                    assert actual_result[0] == expect_result