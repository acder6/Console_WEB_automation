import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class LogicalTable(BasePage):
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')
    # 左边菜单
    logical_loc = (By.XPATH, '//span[@class="el-tree-node__label" and contains(text(), "逻辑库")]')

    # 左边菜单
    logical_table_loc = (By.XPATH, '//span[@class="el-tree-node__label" and contains(text(), "表")]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="新建表"]')

    xg_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and span="修改"]')

    table_struct_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and normalize-space(.//span)="表结构"]')

    table_dist_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and normalize-space(.//span)="表分布"]')

    table_state_input_loc = (By.XPATH, '//textarea[@class="el-textarea__inner"]')

    # 确定按钮
    qd_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and normalize-space(.//span)="确 定"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    size_loc = (By.XPATH, '//span[@class="el-pagination__sizes"]')

    size_xz_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="100条/页"]')

    qd_del_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')


    def create_table(self, jq_name, logical_name,table_state):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalTable.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalTable.logical_loc)
        self.click(LogicalTable.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalTable.logical_table_loc)
        self.click(LogicalTable.logical_table_loc)

        self.wait_click(LogicalTable.register_button_loc)
        self.click(LogicalTable.register_button_loc)

        self.set_keys(LogicalTable.table_state_input_loc, table_state)

        self.click(LogicalTable.qd_loc)

        element = self.wait(LogicalTable.yz_loc)
        if element:
            return self.get_value(LogicalTable.yz_loc)


    def xg_table(self, jq_name, logical_name,table_name,table_xg_state):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        table_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{table_name}")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalTable.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalTable.logical_loc)
        self.click(LogicalTable.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalTable.logical_table_loc)
        self.click(LogicalTable.logical_table_loc)


        self.wait(table_name_loc)
        self.click(table_name_loc)

        self.click(LogicalTable.xg_button_loc)

        self.set_keys(LogicalTable.table_state_input_loc, table_xg_state)

        self.click(LogicalTable.qd_loc)

        element = self.wait(LogicalTable.yz_loc)
        if element:
            return self.get_value(LogicalTable.yz_loc)

    def view_table_struct(self, jq_name, logical_name,table_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        table_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{table_name}")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalTable.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalTable.logical_loc)
        self.click(LogicalTable.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalTable.logical_table_loc)
        self.click(LogicalTable.logical_table_loc)

        self.wait(table_name_loc)
        self.click(table_name_loc)

        self.click(LogicalTable.table_struct_button_loc)

        return self.get_bx_value(LogicalTable.table_state_input_loc)

    def view_table_dist(self, jq_name, logical_name,table_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        table_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{table_name}")]')
        database_table_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{table_name}"]/ancestor::tr//td[6]/div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalTable.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalTable.logical_loc)
        self.click(LogicalTable.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalTable.logical_table_loc)
        self.click(LogicalTable.logical_table_loc)

        self.wait(table_name_loc)
        self.click(table_name_loc)

        self.click(LogicalTable.table_dist_button_loc)

        return self.get_value(database_table_loc)

    def delete_table(self, jq_name, logical_name,table_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        del_loc = (By.XPATH,f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{table_name}")]]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(LogicalTable.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait(LogicalTable.logical_loc)
        self.click(LogicalTable.logical_loc)

        self.wait(logical_name_loc)
        self.click(logical_name_loc)

        self.wait(LogicalTable.logical_table_loc)
        self.click(LogicalTable.logical_table_loc)

        self.wait_click(LogicalTable.size_loc)
        self.click(LogicalTable.size_loc)

        self.wait(LogicalTable.size_xz_loc)
        self.click(LogicalTable.size_xz_loc)

        time.sleep(1)

        self.gd_loc(del_loc)

        self.wait(del_loc)
        self.click(del_loc)

        self.click(LogicalTable.qd_del_loc)

        element = self.wait(LogicalTable.yz_loc)
        if element:
            return self.get_value(LogicalTable.yz_loc)


