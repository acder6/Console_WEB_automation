import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class MonitoringPage(BasePage):
    # 页面元素
    # 资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    # 监控中心
    monitoring_loc = (By.XPATH, '//li[@class="el-menu-item" and .="监控中心"]')

    # 注册监控中心
    register_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and .="注册"]')

    # 监控中心地址
    addr_loc = (By.XPATH, '//label[@for="monitorIp"]//following-sibling::div//input[@class="el-input__inner"]')

    # 监控中心端口
    port_loc = (By.XPATH, '//label[@for="port"]//following-sibling::div//input[@class="el-input__inner"]')

    # 监控中心名称
    monitor_name_loc = (By.XPATH, '//label[@for="monitorName"]//following-sibling::div//input[@class="el-input__inner"]')

    # 确定按钮
    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and .="确 定"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    # 描述
    mx_loc = (By.XPATH, '//label[@for="description"]//following-sibling::div//textarea[@class="el-textarea__inner"]')

    delete_qd_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    def register_monitoring(self,addr,port,monitoring_name):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(MonitoringPage.resource_loc)
        # 点击监控中心
        self.click(MonitoringPage.monitoring_loc)
        # 点击注册监控中心
        self.click(MonitoringPage.register_loc)

        self.set_keys(MonitoringPage.addr_loc,addr)
        self.set_keys(MonitoringPage.port_loc, port)
        self.set_keys(MonitoringPage.monitor_name_loc,monitoring_name)

        self.click(MonitoringPage.register_button_loc)

        element = self.wait(MonitoringPage.yz_loc)
        if element:
            return self.get_value(MonitoringPage.yz_loc)


    def th_monitoring(self,monitoring_name):
        th_monitoring_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{monitoring_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "探活")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(MonitoringPage.resource_loc)
        # 点击监控中心
        self.click(MonitoringPage.monitoring_loc)

        time.sleep(1)
        self.wait_click(th_monitoring_loc)
        self.click(th_monitoring_loc)

        element = self.wait(MonitoringPage.yz_loc)
        if element:
            return self.get_value(MonitoringPage.yz_loc)


    def xg_monitoring(self,monitoring_name,mx):
        xg_monitoring_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{monitoring_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        yz_xg_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{monitoring_name}"]/ancestor::tr/td[8]//div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(MonitoringPage.resource_loc)
        # 点击监控中心
        self.click(MonitoringPage.monitoring_loc)

        time.sleep(1)
        self.wait_click(xg_monitoring_loc)
        self.click(xg_monitoring_loc)

        self.clear(MonitoringPage.mx_loc)
        self.set_keys(MonitoringPage.mx_loc,mx)

        self.click(MonitoringPage.register_button_loc)

        element = self.wait(yz_xg_loc)
        if element:
            return self.get_value(yz_xg_loc)

    def delete_monitoring(self,monitoring_name):
        delete_monitoring_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{monitoring_name}"]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "注销")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(MonitoringPage.resource_loc)
        # 点击监控中心
        self.click(MonitoringPage.monitoring_loc)

        time.sleep(1)
        self.wait_click(delete_monitoring_loc)
        self.click(delete_monitoring_loc)

        self.wait_click(MonitoringPage.delete_qd_loc)
        self.click(MonitoringPage.delete_qd_loc)

        element = self.wait(MonitoringPage.yz_loc)
        if element:
            return self.get_value(MonitoringPage.yz_loc)


