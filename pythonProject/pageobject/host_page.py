import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class HostPage(BasePage):
    # 页面元素
    # 资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    # 主机
    host_loc = (By.XPATH, '//li[@class="el-menu-item" and .="主机"]')

    # 单台注册主机
    register_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    # 主机ip
    ip_loc = (By.XPATH, '//label[@for="hostIp"]//following-sibling::div//input[@class="el-input__inner"]')

    # 主机用户
    username_loc = (By.XPATH, '//label[@for="username"]//following-sibling::div//input[@class="el-input__inner"]')

    # 用户口令
    password_loc = (By.XPATH, '//label[@for="password"]//following-sibling::div//input[@class="el-input__inner"]')

    # SSH端口号
    port_loc = (By.XPATH, '//label[@for="adminPort"]//following-sibling::div//input[@class="el-input__inner"]')

    # 主机名称端口号
    host_name_loc = (By.XPATH, '//label[@for="hostName"]//following-sibling::div//input[@class="el-input__inner"]')

    # 注册数据库按钮
    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    # 完成注册
    sussess_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and ./span="完成注册"]')

    xg_loc = (By.XPATH,
              '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item" and contains(text(), "修改")]')

    delete_loc = (By.XPATH,
              '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item del-operation" and contains(text(), "删除")]')

    qd_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    del_yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    def add_host(self,ip,username,password,port):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(HostPage.resource_loc)
        # 点击主机
        self.click(HostPage.host_loc)
        # 点击注册主机
        self.click(HostPage.register_loc)
        # 填写主机信息
        # ip
        self.set_keys(HostPage.ip_loc, ip)

        # 用户名
        self.set_keys(HostPage.username_loc, username)
        # 密码
        self.set_keys(HostPage.password_loc, password)
        # 端口
        self.set_keys(HostPage.port_loc, port)
        # 注册数据库
        self.click(HostPage.register_button_loc)
        try:
            # 等待注册成功
            self.wait(HostPage.sussess_loc)
            time.sleep(1)

            # 点击完成注册
            self.click(HostPage.sussess_loc)
            print("注册主机成功")
        except TimeoutException:
            print("注册主机失败")


    def xg_host(self,host_name,host_ip):
        xlk_loc = (By.XPATH,
                   f'//div[@class="el-table__fixed-body-wrapper"]//div[@class="cell" and normalize-space()="{host_ip}"]/ancestor::tr/td[last()]//span[@class="el-dropdown-link el-dropdown-selfdefine"]')
        yz_loc = (By.XPATH,
                   f'//div[@class="el-table__body-wrapper is-scrolling-left"]//div[@class="cell" and normalize-space()="{host_ip}"]/ancestor::tr/td[1]/div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(HostPage.resource_loc)
        # 点击主机
        self.click(HostPage.host_loc)

        # 点击下拉框
        time.sleep(1)
        self.wait_click(xlk_loc)
        self.click(xlk_loc)

        # 点击修改
        self.wait_click(HostPage.xg_loc)
        self.click(HostPage.xg_loc)

        self.click(HostPage.qd_loc)

        self.clear(HostPage.host_name_loc)
        self.set_keys(HostPage.host_name_loc, host_name)

        self.click(HostPage.register_button_loc)

        element = self.wait(yz_loc)
        if element:
            return self.get_value(yz_loc)

    def delete_host(self,host_ip):
        xlk_loc = (By.XPATH,
                   f'//div[@class="el-table__fixed-body-wrapper"]//div[@class="cell" and normalize-space()="{host_ip}"]/ancestor::tr/td[last()]//span[@class="el-dropdown-link el-dropdown-selfdefine"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(HostPage.resource_loc)
        # 点击主机
        self.click(HostPage.host_loc)

        # 点击下拉框
        time.sleep(1)
        self.wait_click(xlk_loc)
        self.click(xlk_loc)

        # 点击删除
        self.wait_click(HostPage.delete_loc)
        self.click(HostPage.delete_loc)

        self.click(HostPage.qd_loc)

        element = self.wait(HostPage.del_yz_loc)
        if element:
            return self.get_value(HostPage.del_yz_loc)



