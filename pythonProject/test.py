import os
import unittest
import tkinter as tk
import webbrowser
from HTMLTestRunner import HTMLTestRunner

from base.base_login import BaseLogin

class TaskInputWindow:
    def __init__(self, master, task_name):
        self.master = master
        self.task_name = task_name

        self.top = tk.Toplevel(master)
        self.top.title(f"输入 {task_name} 的参数,如果不输入，则使用默认参数")

        # 添加输入框
        self.login_name_label = tk.Label(self.top, text="用户名:")
        self.login_name_label.pack()
        self.login_name_entry = tk.Entry(self.top)
        self.login_name_entry.pack()

        self.login_password_label = tk.Label(self.top, text="密码:")
        self.login_password_label.pack()
        self.login_password_entry = tk.Entry(self.top, show="* ")
        self.login_password_entry.pack()

        # 添加测试按钮
        self.test_button = tk.Button(self.top, text="测试", command=self.perform_test)
        self.test_button.pack(pady=10)

    def perform_test(self):
        login_name = self.login_name_entry.get()
        login_password = self.login_password_entry.get()
        if login_name !="":
            BaseLogin.login_name = login_name
        if login_password !="":
            BaseLogin.login_password = login_password
        run_tests(self.task_name)
        self.top.destroy()

def run_tests(task):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    testcase_dir = os.path.join(current_dir, "testcase")
    # 获取当前执行文件的目录
    # 构建测试脚本的路径
    suite = unittest.defaultTestLoader.discover(testcase_dir, f"{task}.py")  # 替换为你的测试脚本文件名

    # 构建报告文件的路径
    report_dir = os.path.join(current_dir, "report")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    report_file_path = os.path.join(report_dir, "report.html")
    print("报告文件路径:", report_file_path)

    # 生成html报告文件
    report_file = open(report_file_path, "wb")

    # s生成一个HTMLTestRunner对象
    runner = HTMLTestRunner(stream=report_file, title="Console自动化测试报告", description="测试结果")

    # 执行测试用例
    runner.run(suite)

    # 关闭报告文件
    report_file.close()

    # 尝试打开报告文件
    webbrowser.open(report_file_path)




def perform_task(task_name):
    global selected_task
    selected_task = task_name
    if task_name == "退出":
        root.quit()
        root.destroy()
        exit(0)
    # root.quit()
    # root.destroy()
    TaskInputWindow(root, task_name)
def get_task():
    global root, selected_task
    selected_task = None
    root = tk.Tk()
    root.title("选择测试任务")
    options = {
        "登录测试": "test_01_login",
        "注册主机测试": "test_02_host",
        "注册数据库测试": "test_03_adbase",
        "管理数据库测试": "test_04_control_db",
        "治理中心测试": "test_05_govern",
        "监控中心测试": "test_06_monitoring",
        "日志中心测试": "test_07_log",
        "添加集群测试": "test_08_addcluster",
        "管理集群测试": "test_09_control_cluster",
        "规则测试": "test_10_rule",
        "规则组测试": "test_11_rulegroup",
        "脱敏策略测试": "test_12_tm_strategy",
        "加密策略测试": "test_13_jm_strategy",
        "加密后缀测试": "test_14_jm_suff",
        "添加存储节点测试": "test_15_add_storge_node",
        "管理存储节点测试": "test_16_control_storge_node",
        "参数测试": "test_17_paramter",
        "配置监控测试": "test_18_conf_monitoring",
        "查看监控测试": "test_19_view_monitoring",
        "配置日志测试": "test_20_conf_log",
        "所有测试": "*",
        "退出":"退出",
    }
    def create_button(option, task_name):
        # 创建按钮并捕获当前的 task_name
        button = tk.Button(root, text=option, command=lambda: perform_task(task_name))
        button.pack(pady=5)

    for option, task_name in options.items():
        create_button(option, task_name)

    root.mainloop()
    return selected_task

root = tk.Tk()
root.withdraw()
while True:
    task = get_task()
    print(task)
    if task == "退出":
        print("没有选择任何测试任务，程序将退出。")
        break
    else:
        run_tests(task)
