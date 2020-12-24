#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 5:00 PM
# @Author  : cherry
# @Email   : xiaoyin_1116@163.com
# @File    : project_path.py
# @Software: PyCharm

import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
test_login_path=os.path.join(project_path,'data','test_login.yml')
test_zhibo_path=os.path.join(project_path,'data','test_zhibo.yml')
test_path=os.path.join(project_path,'data','test.yml')
env_path=os.path.join(project_path,'config','env.yml')