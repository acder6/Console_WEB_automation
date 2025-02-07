import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class SqlManagementLog(BasePage):

    sql_management_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="SQL 管理"]')
    # 慢日志
    log_loc = (By.XPATH, '//li[@class="el-menu-item" and .="慢日志"]')

    derive_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="导出"]')

    screnn_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="查询"]')

    cluster_loc = (By.XPATH, '//label[.="集群管理"]//following-sibling::div//input[@class="el-input__inner"]')

    logical_loc = (By.XPATH, '//label[.="逻辑库"]//following-sibling::div//input[@class="el-input__inner"]')

    sqltype_loc = (By.XPATH, '//label[.="SQL类型"]//following-sibling::div//input[@class="el-input__inner"]')

    # alter_type_loc = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="ALTER"]')

    download_path = 'D:\\test_downlode\\'  # 你的下载路径
    expected_filename = 'slowSql.csv'  # 预期的文件名

    def view_log(self, jq_name, logical_name,sql_type):
        jq_name_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{jq_name}"]')
        logical_name_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{logical_name}"]')
        sql_type_loc = (By.XPATH,
                          f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{sql_type}"]')

        yz_log_loc = (
        By.XPATH, f'//div[@class="cell" and normalize-space()="{logical_name}"]/ancestor::tr/td[5]/div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(SqlManagementLog.sql_management_loc)

        self.wait_click(SqlManagementLog.log_loc)
        self.click(SqlManagementLog.log_loc)

        self.wait_click(SqlManagementLog.cluster_loc)
        self.click(SqlManagementLog.cluster_loc)

        try:
            self.wait_click(jq_name_loc)
            self.click(jq_name_loc)
        except TimeoutException:
            print(f'{jq_name}已选中')

        self.wait_click(SqlManagementLog.logical_loc)
        self.click(SqlManagementLog.logical_loc)

        self.wait_click(logical_name_loc)
        self.click(logical_name_loc)

        self.wait_click(SqlManagementLog.sqltype_loc)
        self.click(SqlManagementLog.sqltype_loc)

        self.wait_click(sql_type_loc)
        self.click(sql_type_loc)

        self.wait_click(SqlManagementLog.screnn_loc)
        self.click(SqlManagementLog.screnn_loc)

        time.sleep(1)
        self.wait(yz_log_loc)
        return self.get_value(yz_log_loc)

    def derive_log(self, jq_name, logical_name,sql_type):
        jq_name_loc = (By.XPATH,
                       f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{jq_name}"]')
        logical_name_loc = (By.XPATH,
                            f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{logical_name}"]')

        sql_type_loc = (By.XPATH,
                          f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{sql_type}"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(SqlManagementLog.sql_management_loc)

        self.wait_click(SqlManagementLog.log_loc)
        self.click(SqlManagementLog.log_loc)

        self.wait_click(SqlManagementLog.cluster_loc)
        self.click(SqlManagementLog.cluster_loc)

        try:
            self.wait_click(jq_name_loc)
            self.click(jq_name_loc)
        except TimeoutException:
            print(f'{jq_name}已选中')

        self.wait_click(SqlManagementLog.logical_loc)
        self.click(SqlManagementLog.logical_loc)

        self.wait_click(logical_name_loc)
        self.click(logical_name_loc)

        self.wait_click(SqlManagementLog.sqltype_loc)
        self.click(SqlManagementLog.sqltype_loc)

        self.wait_click(sql_type_loc)
        self.click(sql_type_loc)

        self.wait_click(SqlManagementLog.screnn_loc)
        self.click(SqlManagementLog.screnn_loc)

        time.sleep(1)
        self.wait(SqlManagementLog.derive_loc)
        self.click(SqlManagementLog.derive_loc)

        time.sleep(1)

        file_path = os.path.join(SqlManagementLog.download_path, SqlManagementLog.expected_filename)

        # 验证文件是否存在
        if os.path.exists(file_path):
            print("文件下载成功:", file_path)
            self.clear_downlode_file(SqlManagementLog.download_path, SqlManagementLog.expected_filename)
            return True
        else:
            print("文件下载失败:", file_path)
            return False




