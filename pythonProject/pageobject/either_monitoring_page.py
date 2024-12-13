import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class EitherMonitoringPage(BasePage):
    # 资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    # 主机
    host_loc = (By.XPATH, '//li[@class="el-menu-item" and .="主机"]')

    # 数据库
    database_loc = (By.XPATH, '//li[@class="el-menu-item" and .="数据库"]')

    # 集群
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')

    # 配置监控按钮
    conf_monitoring_loc = (By.XPATH,'//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item" and contains(text(), "配置监控")]')

    #监控中心地址下拉框
    addr_moni_xlk_loc = (By.XPATH, '//label[@for="monitorId"]//following-sibling::div//input[@class="el-input__inner" and @readonly="readonly"]')

    #监控标签
    label_moni_loc = (By.XPATH, '//label[@for="monitorLabel"]//following-sibling::div//input[@class="el-input__inner"]')

    #确定按钮
    qd_loc = (By.XPATH, '//button[@class="el-button el-button--default"]//following-sibling::button[@class="el-button el-button--primary"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    cluster_monitoring_loc = (By.ID, 'tab-fifith')

    #集群监控标签
    label_cluster_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="58.210.177.75"]/ancestor::tr//input[@class="el-input__inner"]')



    def conf_monitoring_host(self,host_ip, monitoring_addr, label):
        xlk_host_loc = (By.XPATH,
                   f'//div[@class="el-table__fixed-body-wrapper"]//div[@class="cell" and normalize-space()="{host_ip}"]/ancestor::tr/td[last()]//span[@class="el-dropdown-link el-dropdown-selfdefine"]')

        # 监控中心地址
        addr_moni_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{monitoring_addr}"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(EitherMonitoringPage.resource_loc)
        # 点击主机
        self.click(EitherMonitoringPage.host_loc)

        self.wait(xlk_host_loc)
        self.wait_click(xlk_host_loc)
        self.click(xlk_host_loc)

        self.wait_click(EitherMonitoringPage.conf_monitoring_loc)
        self.click(EitherMonitoringPage.conf_monitoring_loc)

        self.wait(EitherMonitoringPage.addr_moni_xlk_loc)
        self.click(EitherMonitoringPage.addr_moni_xlk_loc)

        self.wait_click(addr_moni_loc)
        self.click(addr_moni_loc)


        self.set_keys(EitherMonitoringPage.label_moni_loc, label)

        self.click(EitherMonitoringPage.qd_loc)

        element = self.wait(EitherMonitoringPage.yz_loc)
        if element:
            return self.get_value(EitherMonitoringPage.yz_loc)


    def conf_monitoring_database(self,database_name, monitoring_addr, label):
        xlk_db_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{database_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')

        # 监控中心地址
        addr_moni_loc = (By.XPATH,
                         f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{monitoring_addr}"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)
        # 点击资源管理
        self.click(EitherMonitoringPage.resource_loc)
        # 点击数据库
        self.click(EitherMonitoringPage.database_loc)
        # 数据库配置监控

        self.wait_click(xlk_db_loc)
        self.click(xlk_db_loc)

        self.wait_click(EitherMonitoringPage.conf_monitoring_loc)
        self.click(EitherMonitoringPage.conf_monitoring_loc)

        self.wait(EitherMonitoringPage.addr_moni_xlk_loc)
        self.click(EitherMonitoringPage.addr_moni_xlk_loc)

        self.wait_click(addr_moni_loc)
        self.click(addr_moni_loc)

        self.set_keys(EitherMonitoringPage.label_moni_loc, label)

        self.click(EitherMonitoringPage.qd_loc)

        element = self.wait(EitherMonitoringPage.yz_loc)
        if element:
            return self.get_value(EitherMonitoringPage.yz_loc)

    def conf_monitoring_cluster(self,cluster_name, label):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{cluster_name}")]]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(EitherMonitoringPage.cluster_loc)


        self.wait_click(jq_loc)
        self.click(jq_loc)

        self.click(EitherMonitoringPage.cluster_monitoring_loc)

        self.clear(EitherMonitoringPage.label_cluster_loc)
        self.set_keys(EitherMonitoringPage.label_cluster_loc, label)

        self.click(EitherMonitoringPage.qd_loc)

        element = self.wait(EitherMonitoringPage.yz_loc)
        if element:
            return self.get_value(EitherMonitoringPage.yz_loc)

