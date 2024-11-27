import os
import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class LogicalLog(BasePage):
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')
    # 左边菜单
    logical_loc = (By.XPATH, '//span[@class="el-tree-node__label" and contains(text(), "逻辑库")]')

    log_loc = (By.ID, 'tab-fourth')

    derive_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="导出"]')

    screnn_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="查询"]')

    sqltype_loc = (By.XPATH, '//label[.="SQL类型"]//following-sibling::div//input[@class="el-input__inner"]')

    drop_type_loc = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="DROP"]')

    download_path = 'D:\\test_downlode\\'  # 你的下载路径
    expected_filename = 'slowSql.csv'  # 预期的文件名

    def view_logical_log(self, jq_name, logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        yz_log_loc=(By.XPATH,f'//div[@class="cell" and normalize-space()="{logical_name}"]/ancestor::tr/td[5]/div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalLog.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalLog.logical_loc)
        self.click(LogicalLog.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalLog.log_loc)
        self.click(LogicalLog.log_loc)

        self.wait_click(LogicalLog.sqltype_loc)
        self.click(LogicalLog.sqltype_loc)

        self.wait(LogicalLog.drop_type_loc)
        self.click(LogicalLog.drop_type_loc)

        self.wait(LogicalLog.screnn_loc)
        self.click(LogicalLog.screnn_loc)

        time.sleep(1)
        self.wait(yz_log_loc)
        return self.get_value(yz_log_loc)

    def derive_logical_log(self, jq_name, logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalLog.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalLog.logical_loc)
        self.click(LogicalLog.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalLog.log_loc)
        self.click(LogicalLog.log_loc)

        self.click(LogicalLog.sqltype_loc)

        self.wait(LogicalLog.drop_type_loc)
        self.click(LogicalLog.drop_type_loc)

        self.wait(LogicalLog.screnn_loc)
        self.click(LogicalLog.screnn_loc)

        time.sleep(1)
        self.wait(LogicalLog.derive_loc)
        self.click(LogicalLog.derive_loc)

        time.sleep(1)

        file_path = os.path.join(LogicalLog.download_path, LogicalLog.expected_filename)

        # 验证文件是否存在
        if os.path.exists(file_path):
            print("文件下载成功:", file_path)
            self.clear_downlode_file(LogicalLog.download_path, LogicalLog.expected_filename)
            return True
        else:
            print("文件下载失败:", file_path)
            return False