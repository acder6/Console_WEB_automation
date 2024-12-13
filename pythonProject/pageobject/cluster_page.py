import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class ClusterPage(BasePage):


    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    cluster_name_loc = (By.XPATH, '//label[@for="clusterName"]//following-sibling::div//input[@class="el-input__inner"]')

    # ip
    ip_loc = (By.XPATH, '//label[@for="adminIp"]//following-sibling::div//input[@class="el-input__inner"]')

    #port
    port_loc = (By.XPATH, '//label[@for="adminPort"]//following-sibling::div//input[@class="el-input__inner"]')

    #username
    username_loc = (By.XPATH, '//label[@for="adminUsername"]//following-sibling::div//input[@class="el-input__inner"]')

    #password
    password_loc = (By.XPATH, '//label[@for="adminPassword"]//following-sibling::div//input[@class="el-input__inner"]')

    # 完成注册
    sussess_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and ./span="完成注册"]')

    # 数据库类型
    type_box_loc = (By.XPATH, '//input[@class="el-input__inner" and @readonly="readonly"]')

    # PostgreSQL
    pg_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="PostgreSQL"]')

    #左边菜单
    # jq_loc = (By.XPATH,'//span[@class="el-tree-node__label" and contains(text(), "test_0828")]')
    #列表名称
    # jq_loc = (By.XPATH, '//button[@class="el-button el-button--text" and ./span[contains(text(), "test_0828")]]')

    xg_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and ./span[contains(text(), "修改")]]')

    mx_loc = (By.XPATH,'//textarea[@class="el-textarea__inner"]' )

    yz_loc = (By.XPATH, '//div[@class="el-col el-col-4" and contains(text(), "集群描述")]/following-sibling::div[@class="el-col el-col-20"]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')

    yz_d_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')
    def register_m_cluster(self,cluster_name,ip,port,username,password):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterPage.cluster_loc)

        self.wait_click(ClusterPage.register_button_loc)
        self.click(ClusterPage.register_button_loc)

        self.set_keys(ClusterPage.cluster_name_loc, cluster_name)
        self.set_keys(ClusterPage.ip_loc, ip)
        self.set_keys(ClusterPage.port_loc, port)
        self.set_keys(ClusterPage.username_loc, username)
        self.set_keys(ClusterPage.password_loc, password)

        self.click(ClusterPage.register_button_loc)

        try:
            # 等待注册成功
            self.wait_click(ClusterPage.sussess_loc)

            # 点击完成注册
            self.click(ClusterPage.sussess_loc)
            print("注册 MySQL 集群成功")
        except TimeoutException:
            print("注册 MySQL 集群失败")

    def register_pg_cluster(self,cluster_name,ip,port,username,password):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterPage.cluster_loc)

        self.wait_click(ClusterPage.register_button_loc)
        self.click(ClusterPage.register_button_loc)


        self.set_keys(ClusterPage.cluster_name_loc, cluster_name)

        self.click(ClusterPage.type_box_loc)

        self.wait(ClusterPage.pg_loc)
        self.click(ClusterPage.pg_loc)

        self.set_keys(ClusterPage.ip_loc, ip)
        self.set_keys(ClusterPage.port_loc, port)
        self.set_keys(ClusterPage.username_loc, username)
        self.set_keys(ClusterPage.password_loc, password)

        self.click(ClusterPage.register_button_loc)

        try:
            # 等待注册成功
            self.wait_click(ClusterPage.sussess_loc)

            # 点击完成注册
            self.click(ClusterPage.sussess_loc)
            print("注册 PostgreSQL 集群成功")
        except TimeoutException:
            print("注册 PostgreSQL 集群失败")



    def register_ora_cluster(self,cluster_name,ip,port,username,password):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterPage.cluster_loc)

        self.wait_click(ClusterPage.register_button_loc)
        self.click(ClusterPage.register_button_loc)

        self.set_keys(ClusterPage.cluster_name_loc, cluster_name)
        self.set_keys(ClusterPage.ip_loc, ip)
        self.set_keys(ClusterPage.port_loc, port)
        self.set_keys(ClusterPage.username_loc, username)
        self.set_keys(ClusterPage.password_loc, password)

        self.click(ClusterPage.register_button_loc)

        try:
            # 等待注册成功
            self.wait_click(ClusterPage.sussess_loc)

            # 点击完成注册
            self.click(ClusterPage.sussess_loc)
            print("注册 Oracle 集群成功")
        except TimeoutException:
            print("注册 Oracle 集群失败")

    def xg_cluster(self,cluster_name,mx):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{cluster_name}")]]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterPage.cluster_loc)


        self.wait_click(jq_loc)
        self.click(jq_loc)

        self.wait_click(ClusterPage.xg_loc)
        self.click(ClusterPage.xg_loc)

        self.clear(ClusterPage.mx_loc)
        self.set_keys(ClusterPage.mx_loc,mx)
        self.click(ClusterPage.register_button_loc)

        time.sleep(1)

        element = self.wait(ClusterPage.yz_loc)
        if element:
            return self.get_value(ClusterPage.yz_loc)

    def del_cluster(self,cluster_name):

        del_loc = (By.XPATH,f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{cluster_name}")]]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ClusterPage.cluster_loc)



        self.wait_click(del_loc)
        self.click(del_loc)

        self.wait(ClusterPage.qr_loc)
        self.click(ClusterPage.qr_loc)


        element = self.wait(ClusterPage.yz_d_loc)
        if element:
            return self.get_value(ClusterPage.yz_d_loc)

