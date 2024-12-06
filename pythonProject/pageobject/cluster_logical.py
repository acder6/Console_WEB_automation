import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage



class ClusterLogical(BasePage):
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')
    # 左边菜单
    logical_loc = (By.XPATH,'//span[@class="el-tree-node__label" and contains(text(), "逻辑库")]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    # 逻辑库名称
    database_name_loc = (By.XPATH, '//label[@for="databaseName"]//following-sibling::div//input[@class="el-input__inner"]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确 定")]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    qd_del_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')

    xz_kx_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "可选节点")]')

    xz_yx_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "已选节点")]')

    yd_loc = (By.XPATH, '//button[@class="el-button el-button--primary el-transfer__button"]')
    def add_cluster_logical(self,jq_name,logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterLogical.cluster_loc)

        time.sleep(1)
        self.wait_click(jq_loc)
        self.click(jq_loc)

        self.wait_click(ClusterLogical.logical_loc)
        self.click(ClusterLogical.logical_loc)

        time.sleep(1)
        self.click(ClusterLogical.register_button_loc)

        self.set_keys(ClusterLogical.database_name_loc, logical_name)

        self.wait_click(ClusterLogical.qd_button_loc)
        self.click(ClusterLogical.qd_button_loc)


        element = self.wait(ClusterLogical.yz_loc)
        if element:
            return self.get_value(ClusterLogical.yz_loc)


    def add_node_database(self, jq_name, logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterLogical.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait_click(ClusterLogical.logical_loc)
        self.click(ClusterLogical.logical_loc)

        self.wait_click(logical_name_loc)
        self.click(logical_name_loc)

        self.click(ClusterLogical.xz_kx_loc)

        self.click(ClusterLogical.yd_loc)

        self.click(ClusterLogical.qd_button_loc)

        element = self.wait(ClusterLogical.yz_loc)
        if element:
            return self.get_value(ClusterLogical.yz_loc)

    def del_node_database(self, jq_name, logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        logical_name_loc = (By.XPATH, f'//span[@class="el-tree-node__label" and contains(text(), "{logical_name}")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterLogical.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.wait_click(ClusterLogical.logical_loc)
        self.click(ClusterLogical.logical_loc)

        self.wait_click(logical_name_loc)
        self.click(logical_name_loc)

        self.click(ClusterLogical.xz_yx_loc)

        self.click(ClusterLogical.yd_loc)

        self.click(ClusterLogical.qd_button_loc)

        element = self.wait(ClusterLogical.yz_loc)
        if element:
            return self.get_value(ClusterLogical.yz_loc)

    def del_cluster_logical(self, jq_name, logical_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        del_loc = (By.XPATH,
                   f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{logical_name}")]]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterLogical.cluster_loc)

        time.sleep(1)
        self.wait_click(jq_loc)
        self.click(jq_loc)

        self.wait_click(ClusterLogical.logical_loc)
        self.click(ClusterLogical.logical_loc)

        self.wait_click(del_loc)
        self.click(del_loc)

        self.wait_click(ClusterLogical.qd_del_loc)
        self.click(ClusterLogical.qd_del_loc)

        element = self.wait(ClusterLogical.yz_loc)
        if element:
            return self.get_value(ClusterLogical.yz_loc)