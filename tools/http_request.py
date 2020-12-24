#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:25 AM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : http_request.py
# @Software: PyCharm

import requests
# import logging
# import requests.packages.urllib3
# import ssl
# from requests_toolbelt import SSLAdapter

class HttpRequest:
    def http_request(self,url,data,http_method,token):
        header={"Content-Type":"application/json","token":token}

        try:
            if http_method.upper()=='GET':
                res=requests.get(url,json=data,verify=False,headers=header)
            elif http_method.upper()=='POST':
                res=requests.post(url,json=data,verify=False,headers=header)
            elif http_method.upper()=='PUT':
                res=requests.put(url,json=data,verify=False,headers=header)
            elif http_method.upper()=='DELETE':
                res=requests.delete(url,json=data,verify=False,headers=header)
            elif http_method.upper()=='PATCH':
                res=requests.patch(url,json=data,verify=False,headers=header)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了：{0}".format(e))
            raise e
        return res