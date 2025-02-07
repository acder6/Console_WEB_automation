import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class DatabasePage(BasePage):

    #页面元素
    #资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    #数据库
    database_loc = (By.XPATH, '//li[@class="el-menu-item" and .="数据库"]')

    #注册数据库
    register_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    #ip
    ip_loc = (By.XPATH, '//label[@for="ip"]//following-sibling::div//input[@class="el-input__inner"]')

    #端口号
    port_loc = (By.XPATH, '//label[@for="port"]//following-sibling::div//input[@class="el-input__inner"]')

    #数据库类型
    type_box_loc = (By.XPATH, '//input[@class="el-input__inner" and @readonly="readonly"]')

    #用户名
    username_loc = (By.XPATH, '//label[@for="username"]//following-sibling::div//input[@class="el-input__inner"]')

    #密码
    password_loc = (By.XPATH, '//label[@for="password"]//following-sibling::div//input[@class="el-input__inner"]')

    #注册数据库按钮
    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    #完成注册
    sussess_loc = (By.XPATH,'//button[@class="el-button el-button--primary" and ./span="完成注册"]')

    #pg数据库的名称
    database_name_loc = (By.XPATH, '//label[@for="databaseName"]//following-sibling::div//input[@class="el-input__inner"]')

    #oracle的sid
    sid_loc = (By.XPATH, '//label[@class="el-radio" and .="SID"]')

    #sid输入框
    sid_input_loc = (By.XPATH, '//div[@class="el-form-item el-form-item--feedback"]//following-sibling::div[1]//input[@class="el-input__inner"]')

    #mysql
    mysql_loc = (By.XPATH, '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="MySQL"]')

    #PostgreSQL
    pg_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="PostgreSQL"]')

    #Oracle
    ora_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="Oracle"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    xg_loc = (By.XPATH, '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item" and contains(text(), "修改")]')

    delete_loc = (By.XPATH, '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item del-operation" and contains(text(), "删除")]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')

    #添加Mysql数据库
    def add_m_database(self,ip,port,username,password):

        #登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        #添加数据库步骤
        # 点击资源管理
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)
        # 点击注册数据库
        self.click(DatabasePage.register_loc)
        # 填写数据库信息
        #ip
        self.set_keys(DatabasePage.ip_loc,ip)
        # 端口
        self.set_keys(DatabasePage.port_loc,port)
        # 数据库类型
        self.click(DatabasePage.type_box_loc)
        # 选择数据库类型
        self.wait(DatabasePage.mysql_loc)
        self.click(DatabasePage.mysql_loc)
        # 用户名
        self.set_keys(DatabasePage.username_loc,username)
        # 密码
        self.set_keys(DatabasePage.password_loc,password)
        # 注册数据库
        self.click(DatabasePage.register_button_loc)
        try:
            # 等待注册成功
            self.wait(DatabasePage.sussess_loc)
            time.sleep(1)

            # 点击完成注册
            self.click(DatabasePage.sussess_loc)
            print("注册 MySQL 数据库成功")
        except TimeoutException:
            print("注册 MySQL 数据库失败")

    # 添加PostgreSQL数据库
    def add_pg_database(self,ip,port,username,password,database_name):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # time.sleep(3)
        # 添加数据库步骤
        # 点击资源管理
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)
        # 点击注册数据库
        self.click(DatabasePage.register_loc)
        # 填写数据库信息
        # ip
        self.set_keys(DatabasePage.ip_loc, ip)
        # 端口
        self.set_keys(DatabasePage.port_loc, port)
        # 数据库类型
        self.click(DatabasePage.type_box_loc)
        # 选择数据库类型
        self.wait_click(DatabasePage.pg_loc)
        self.click(DatabasePage.pg_loc)
        time.sleep(1)
        # 用户名
        self.set_keys(DatabasePage.username_loc, username)
        # 密码
        self.set_keys(DatabasePage.password_loc, password)
        # 数据库名称
        self.set_keys(DatabasePage.database_name_loc,database_name)
        # 注册数据库
        self.click(DatabasePage.register_button_loc)
        try:
            # 等待注册成功
            self.wait(DatabasePage.sussess_loc)
            time.sleep(1)
            # 点击完成注册

            self.click(DatabasePage.sussess_loc)
            print("注册 PostgreSQL 数据库成功")
        except TimeoutException:
            print("注册 PostgreSQL 数据库失败")

    # 添加Oracle数据库
    def add_ora_database(self,ip,port,sid_name,username,password):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)
        # time.sleep(3)
        # 添加数据库步骤
        # 点击资源管理
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)
        # 点击注册数据库
        self.click(DatabasePage.register_loc)
        # 填写数据库信息
        # ip
        self.set_keys(DatabasePage.ip_loc, ip)
        # 端口
        self.set_keys(DatabasePage.port_loc, port)
        # 数据库类型
        self.click(DatabasePage.type_box_loc)
        # 选择数据库类型
        self.wait_click(DatabasePage.ora_loc)
        self.click(DatabasePage.ora_loc)
        # sid
        # self.wait_click(DatabasePage.sid_loc)
        # self.click(DatabasePage.sid_loc)
        # sid
        self.set_keys(DatabasePage.sid_input_loc,sid_name)
        # 用户名
        self.set_keys(DatabasePage.username_loc, username)
        # 密码
        self.set_keys(DatabasePage.password_loc, password)
        # 注册数据库
        self.click(DatabasePage.register_button_loc)
        try:
            # 等待注册成功
            self.wait(DatabasePage.sussess_loc)
            time.sleep(1)

            # 点击完成注册
            self.click(DatabasePage.sussess_loc)
            print("注册 Oracle 数据库成功")
        except TimeoutException:
            print("注册 Oracle 数据库失败")


    #探活数据库
    def th_m_database(self, database_name):
        th_loc_mysql = (By.XPATH,f'//div[@class="cell" and normalize-space()="{database_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "探活")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)
        # 点击资源管理
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)
        # 数据库探活
        time.sleep(1)
        self.wait(th_loc_mysql)
        self.click(th_loc_mysql)

        element = self.wait(DatabasePage.yz_loc)
        if element:
            return self.get_value(DatabasePage.yz_loc)

    #修改数据库
    def xg_m_database(self,database_name,ip):
        xlk_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{database_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')
        ip_yz_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{database_name}"]/ancestor::tr//td[1]/div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)
        # 点击资源管理
        self.wait(DatabasePage.resource_loc)
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)

        # 点击下拉框
        time.sleep(1)
        self.wait_click(xlk_loc)
        self.click(xlk_loc)

        # 点击修改
        self.wait_click(DatabasePage.xg_loc)
        self.click(DatabasePage.xg_loc)

        # 修改ip
        # 清除ip
        self.clear(DatabasePage.ip_loc)
        # 输入ip
        self.set_keys(DatabasePage.ip_loc, ip)

        self.click(DatabasePage.register_button_loc)

        element = self.wait(ip_yz_loc)
        if element:
            return self.get_value(ip_yz_loc)


    #删除数据库
    def delete_m_database(self, database_name):
        xlk_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{database_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)
        # 点击资源管理
        self.wait(DatabasePage.resource_loc)
        self.click(DatabasePage.resource_loc)
        # 点击数据库
        self.click(DatabasePage.database_loc)

        # 点击下拉框
        time.sleep(1)
        self.wait_click(xlk_loc)
        self.click(xlk_loc)

        # 点击删除
        self.wait_click(DatabasePage.delete_loc)
        self.click(DatabasePage.delete_loc)

        #点击确认
        self.wait_click(DatabasePage.qr_loc)
        self.click(DatabasePage.qr_loc)

        element = self.wait(DatabasePage.yz_loc)
        if element:
            return self.get_value(DatabasePage.yz_loc)
