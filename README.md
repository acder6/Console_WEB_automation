该脚本使用Selenium工具 + Unittest框架 + HTMLTestRunner文件作为Console的Web自动化脚本,目前该脚本覆盖功能模块：资源管理、集群管理（集群、逻辑库、表）、SQL 管理（防火墙除外）、监控、敏感数据识别（规则）、系统配置,base文件夹下为封装好的Selenium的方法和相关初始化文件，pageobject文件夹下为不同功能的详细操作代码与定位元素，testcase文件夹下是具体测试用例，report文件夹下是生成的测试报告，安装selenium和相关测试浏览器后，HTMLTestRunner文件放入python的lib文件下，启动all.py文件



！！！Selenium版本4.23.1
！！！chrome版本是127.0.6533.119的测试版
