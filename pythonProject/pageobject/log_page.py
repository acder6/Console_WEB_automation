import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class LogPage(BasePage):
    # 页面元素
    # 资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    # 日志中心
    log_loc = (By.XPATH, '//li[@class="el-menu-item" and .="日志中心"]')

    # 注册日志中心
    register_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and .="注册"]')

    # 日志中心地址
    addr_loc = (By.XPATH, '//label[@for="address"]//following-sibling::div//input[@class="el-input__inner"]')

    # 日志中心名称
    log_name_loc = (
    By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    # 确定按钮
    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    th_loc = (By.XPATH, '//button[@class="el-button el-button--text" and contains(., "探活")]')

    # 描述
    mx_loc = (By.XPATH, '//label[@for="description"]//following-sibling::div//textarea[@class="el-textarea__inner"]')

    delete_qd_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    def register_Log(self,addr,log_name):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(LogPage.resource_loc)
        # 点击日志中心
        self.click(LogPage.log_loc)
        # 点击注册日志中心
        self.click(LogPage.register_loc)

        self.set_keys(LogPage.addr_loc,addr)
        self.set_keys(LogPage.log_name_loc,log_name)

        self.click(LogPage.register_button_loc)

        element = self.wait(LogPage.yz_loc)
        if element:
            return self.get_value(LogPage.yz_loc)


    def eith_node_th_log(self,log_name):
        eith_node_log_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{log_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "管理节点")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(LogPage.resource_loc)
        # 点击日志中心
        self.click(LogPage.log_loc)

        self.click(eith_node_log_loc)

        time.sleep(2)
        self.click(LogPage.th_loc)

        element = self.wait(LogPage.yz_loc)
        if element:
            return self.get_value(LogPage.yz_loc)


    def xg_log(self,log_name,mx):
        xg_log_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{log_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        yz_xg_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{log_name}"]/ancestor::tr/td[3]//div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(LogPage.resource_loc)
        # 点击日志中心
        self.click(LogPage.log_loc)

        time.sleep(1)
        self.wait_click(xg_log_loc)
        self.click(xg_log_loc)

        self.clear(LogPage.mx_loc)
        self.set_keys(LogPage.mx_loc,mx)

        self.click(LogPage.register_button_loc)

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
        self.click(LogPage.resource_loc)
        # 点击日志中心
        self.click(LogPage.log_loc)

        time.sleep(1)
        self.wait_click(delete_monitoring_loc)
        self.click(delete_monitoring_loc)

        self.wait_click(LogPage.delete_qd_loc)
        self.click(LogPage.delete_qd_loc)

        element = self.wait(LogPage.yz_loc)
        if element:
            return self.get_value(LogPage.yz_loc)
