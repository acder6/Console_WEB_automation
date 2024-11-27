import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage




class SqlManagementRouting(BasePage):
    sql_management_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="SQL 管理"]')
    # SQL 路由
    routing_loc = (By.XPATH, '//li[@class="el-menu-item" and .="SQL 路由"]')

    cluster_loc = (By.XPATH, '//label[@for="cluster"]//following-sibling::div//input[@class="el-input__inner"]')

    logical_loc = (By.XPATH, '//label[@for="schema"]//following-sibling::div//input[@class="el-input__inner"]')

    sql_state_loc = (By.XPATH, '//textarea[@class="el-textarea__inner"]')

    view_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    def sql_routing(self,jq_name,logical_name,sql_state):
        jq_name_loc = (By.XPATH,
                       f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{jq_name}"]')
        logical_name_loc = (By.XPATH,
                            f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{logical_name}"]')
        yz_routing_loc = (
            By.XPATH,
            f'//tr[@class="el-table__row"]/td[1]/div[@class="cell"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(SqlManagementRouting.sql_management_loc)

        self.wait_click(SqlManagementRouting.routing_loc)
        self.click(SqlManagementRouting.routing_loc)

        self.wait_click(SqlManagementRouting.cluster_loc)
        self.click(SqlManagementRouting.cluster_loc)

        try:
            self.wait_click(jq_name_loc)
            self.click(jq_name_loc)
        except TimeoutException:
            print(f'{jq_name}已选中')

        self.wait_click(SqlManagementRouting.logical_loc)
        self.click(SqlManagementRouting.logical_loc)

        try:
            self.wait_click(logical_name_loc)
            self.click(logical_name_loc)
        except TimeoutException:
            print(f'{logical_name}已选中')


        self.set_keys(SqlManagementRouting.sql_state_loc, sql_state)

        self.click(SqlManagementRouting.view_button_loc)

        element = self.wait(yz_routing_loc)
        if element:
            return self.get_value(yz_routing_loc)


