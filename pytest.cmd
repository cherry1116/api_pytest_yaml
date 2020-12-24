#项目根目录执行
#运行测试用例
pytest --alluredir=Outputs/Reports
#生成测试报告
allure generate Outputs/Reports -o Outputs/html --clean
#打开测试报告
allure serve Outputs/Reports
allure open -h 127.0.0.1 -p 8083 Outputs/html