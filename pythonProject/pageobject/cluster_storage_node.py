import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class ClusterStorageNode(BasePage):


    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')

    cluster_storage_node_loc = (By.ID, 'tab-second')

    zc_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "注册存储节点")]')

    sl_loc = (By.XPATH, '//label[@for="databaseInstanceId"]//following-sibling::div//input[@class="el-input__inner"]')

    mysql_loc = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and ./span="MySQL | 58.210.177.75:13301"]')

    pg_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and ./span="PostgreSQL | 58.210.177.75:55555"]')

    ora_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and ./span="Oracle | 192.168.10.20:1521"]')

    db_loc = (By.XPATH, '//label[@for="actualDatabaseName"]//following-sibling::div//input[@class="el-input__inner"]')

    node_name_loc = (By.XPATH, '//label[@for="nodeName"]//following-sibling::div//input[@class="el-input__inner"]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确 定")]')

    delete_qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary " and contains(., "确 定")]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')


    def add_m_storage_node(self,jq_name,dbname,node_name):

       jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
       db_xz_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and ./span="{dbname}"]')

       # 登录
       lp = LoginPage(self.driver)
       lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

       self.click(ClusterStorageNode.cluster_loc)

       time.sleep(1)
       self.wait(jq_loc)
       self.click(jq_loc)


       time.sleep(1)
       self.click(ClusterStorageNode.cluster_storage_node_loc)


       self.wait_click(ClusterStorageNode.zc_button_loc)
       self.click(ClusterStorageNode.zc_button_loc)

       self.wait_click(ClusterStorageNode.sl_loc)
       self.click(ClusterStorageNode.sl_loc)

       self.wait_click(ClusterStorageNode.mysql_loc)
       self.click(ClusterStorageNode.mysql_loc)


       self.wait_click(ClusterStorageNode.db_loc)
       self.click(ClusterStorageNode.db_loc)

       self.gd_loc(db_xz_loc)
       self.wait(db_xz_loc)
       self.click(db_xz_loc)

       self.set_keys(ClusterStorageNode.node_name_loc,node_name)

       self.click(ClusterStorageNode.qd_button_loc)

       element = self.wait(ClusterStorageNode.yz_loc)
       if element:
           return self.get_value(ClusterStorageNode.yz_loc)

    def add_pg_storage_node(self,jq_name,node_name):

       jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')

       # 登录
       lp = LoginPage(self.driver)
       lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

       self.click(ClusterStorageNode.cluster_loc)

       time.sleep(1)
       self.wait(jq_loc)
       self.click(jq_loc)


       self.click(ClusterStorageNode.cluster_storage_node_loc)


       self.wait_click(ClusterStorageNode.zc_button_loc)
       self.click(ClusterStorageNode.zc_button_loc)

       self.wait(ClusterStorageNode.sl_loc)
       self.click(ClusterStorageNode.sl_loc)

       self.wait(ClusterStorageNode.pg_loc)
       self.click(ClusterStorageNode.pg_loc)

       self.set_keys(ClusterStorageNode.node_name_loc,node_name)

       self.click(ClusterStorageNode.qd_button_loc)

       element = self.wait(ClusterStorageNode.yz_loc)
       if element:
           return self.get_value(ClusterStorageNode.yz_loc)

    def add_ora_storage_node(self,jq_name,node_name):

       jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')

       # 登录
       lp = LoginPage(self.driver)
       lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

       self.click(ClusterStorageNode.cluster_loc)

       time.sleep(1)
       self.wait(jq_loc)
       self.click(jq_loc)


       self.click(ClusterStorageNode.cluster_storage_node_loc)


       self.wait_click(ClusterStorageNode.zc_button_loc)
       self.click(ClusterStorageNode.zc_button_loc)

       self.wait(ClusterStorageNode.sl_loc)
       self.click(ClusterStorageNode.sl_loc)

       self.wait(ClusterStorageNode.ora_loc)
       self.click(ClusterStorageNode.ora_loc)


       self.set_keys(ClusterStorageNode.node_name_loc,node_name)

       self.click(ClusterStorageNode.qd_button_loc)

       element = self.wait(ClusterStorageNode.yz_loc)
       if element:
           return self.get_value(ClusterStorageNode.yz_loc)

    def th_node_database(self, jq_name,node_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        th_loc_node = (By.XPATH,f'//div[@class="cell" and normalize-space()="{node_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "探活")]')

        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterStorageNode.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ClusterStorageNode.cluster_storage_node_loc)

        # 存储节点探活
        time.sleep(1)
        self.wait(th_loc_node)
        self.click(th_loc_node)

        element = self.wait(ClusterStorageNode.yz_loc)
        if element:
            return self.get_value(ClusterStorageNode.yz_loc)

    def xg_node_database(self, jq_name,node_name,dbname):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        xg_loc_node = (By.XPATH,f'//div[@class="cell" and normalize-space()="{node_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        db_xz_loc = (By.XPATH, f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and ./span="{dbname}"]')
        db_yz_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{node_name}"]/ancestor::tr//td[7]/div[@class="cell"]')

        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterStorageNode.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ClusterStorageNode.cluster_storage_node_loc)

        #
        time.sleep(1)
        self.wait(xg_loc_node)
        self.click(xg_loc_node)

        self.wait(ClusterStorageNode.db_loc)
        self.click(ClusterStorageNode.db_loc)


        self.gd_loc(db_xz_loc)

        time.sleep(1)
        self.wait(db_xz_loc)
        self.click(db_xz_loc)

        self.click(ClusterStorageNode.qd_button_loc)

        time.sleep(3)

        element = self.wait(db_yz_loc)
        if element:
            return self.get_value(db_yz_loc)

    def delete_node_database(self,jq_name, node_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        delete_loc_node = (By.XPATH,f'//div[@class="cell" and normalize-space()="{node_name}"]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')

        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(ClusterStorageNode.cluster_loc)
        self.click(ClusterStorageNode.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ClusterStorageNode.cluster_storage_node_loc)

        #
        time.sleep(1)
        self.wait(delete_loc_node)
        self.click(delete_loc_node)

        self.wait(ClusterStorageNode.delete_qd_button_loc)
        self.click(ClusterStorageNode.delete_qd_button_loc)


        element = self.wait(ClusterStorageNode.yz_loc)
        if element:
            return self.get_value(ClusterStorageNode.yz_loc)


