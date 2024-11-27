import os
import unittest
import webbrowser
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # print("发现测试用例...")
    # print("当前工作目录:", os.getcwd())
    #
    # #执行需要的用例，并且生成HTML格式的自动化测试报告
    # #使用unittest框架
    # suite = unittest.defaultTestLoader.discover("D:\\Python\\WEB_demo\\pythonProject\\testcase","*.py")
    #
    # print("发现的测试用例数量:", suite.countTestCases())
    # #生成html报告文件
    # report_file = open("D:\\Python\\WEB_demo\\pythonProject\\report\\report.html","wb")
    # 获取当前执行文件的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("当前工作目录:", current_dir)

    # 构建测试用例目录的路径
    testcase_dir = os.path.join(current_dir, "testcase")
    print("测试用例目录:", testcase_dir)
    # 执行需要的用例，并且生成HTML格式的自动化测试报告
    suite = unittest.defaultTestLoader.discover(testcase_dir, "*.py")
    print("发现的测试用例数量:", suite.countTestCases())

    # 构建报告文件的路径
    report_dir = os.path.join(current_dir, "report")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    report_file_path = os.path.join(report_dir, "report.html")
    print("报告文件路径:", report_file_path)

    # 生成html报告文件
    report_file = open(report_file_path, "wb")

    #s生成一个HTMLTestRunner对象
    runner = HTMLTestRunner(stream=report_file,title="Console自动化测试报告",description="测试结果")

    #执行测试用例
    runner.run(suite)

    # 关闭报告文件
    report_file.close()

    # # 尝试打开报告文件
    # webbrowser.open(report_file_path)