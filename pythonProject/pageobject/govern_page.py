import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage





class GovernPage(BasePage):
    # 页面元素
    # 资源管理
    resource_loc = (By.XPATH, '//li[@class="el-submenu"]')

    # 治理中心
    govern_loc = (By.XPATH, '//li[@class="el-menu-item" and .="治理中心"]')

    # 注册治理中心
    register_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    # 治理中心类型
    type_box_loc = (By.XPATH, '//input[@class="el-input__inner" and @readonly="readonly"]')

    # zookeeper
    zookeeper_loc = (By.XPATH,
                 '//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="ZooKeeper"]')

    # 治理中心地址
    addr_loc = (By.XPATH, '//label[@for="address"]//following-sibling::div//input[@class="el-input__inner"]')


    # 治理中心名称
    govern_name_loc = (By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    # 确定按钮
    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    xg_loc = (By.XPATH,
              '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item" and contains(text(), "修改")]')

    mx_loc = (By.XPATH,'//label[@for="description"]//following-sibling::div//textarea[@class="el-textarea__inner"]')

    eith_node_loc = (By.XPATH,'//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item" and contains(text(), "管理节点")]')

    th_loc = (By.XPATH,'//button[@class="el-button el-button--text" and .="探活"]')

    delete_loc = (By.XPATH, '//ul[@class="el-dropdown-menu el-popper"][@style!="display: none;"]//li[@class="el-dropdown-menu__item del-operation" and contains(text(), "删除")]')

    qd_loc = (By.XPATH,'//button[@class="el-button el-button--default el-button--small el-button--primary "]')

    def register_govern(self,govern_name,addr):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(GovernPage.resource_loc)
        # 点击治理中心
        self.click(GovernPage.govern_loc)
        # 点击注册治理中心
        self.click(GovernPage.register_loc)

        time.sleep(1)
        self.click(GovernPage.type_box_loc)

        self.wait_click(GovernPage.zookeeper_loc)
        self.click(GovernPage.zookeeper_loc)

        self.set_keys(GovernPage.addr_loc,addr)
        self.set_keys(GovernPage.govern_name_loc,govern_name)

        self.click(GovernPage.register_button_loc)

        element = self.wait(GovernPage.yz_loc)
        if element:
            return self.get_value(GovernPage.yz_loc)

    def xg_govern(self,govern_name,mx):
        xlk_loc = (By.XPATH,
                   f'//div[@class="cell" and normalize-space()="{govern_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')

        yz_xg_loc = (By.XPATH,
                   f'//div[@class="cell" and normalize-space()="{govern_name}"]/ancestor::tr/td[6]//div[@class="cell"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(GovernPage.resource_loc)
        # 点击治理中心
        self.click(GovernPage.govern_loc)

        time.sleep(1)
        self.click(xlk_loc)

        self.wait_click(GovernPage.xg_loc)
        self.click(GovernPage.xg_loc)

        self.clear(GovernPage.mx_loc)
        self.set_keys(GovernPage.mx_loc,mx)

        self.click(GovernPage.register_button_loc)

        element = self.wait(yz_xg_loc)
        if element:
            return self.get_value(yz_xg_loc)

    def eith_node(self,govern_name):
        xlk_loc = (By.XPATH,
                   f'//div[@class="cell" and normalize-space()="{govern_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(GovernPage.resource_loc)
        # 点击治理中心
        self.click(GovernPage.govern_loc)

        time.sleep(1)
        self.click(xlk_loc)

        self.wait_click(GovernPage.eith_node_loc)
        self.click(GovernPage.eith_node_loc)

        time.sleep(1)
        self.click(GovernPage.th_loc)

        element = self.wait(GovernPage.yz_loc)
        if element:
            return self.get_value(GovernPage.yz_loc)

    def delete_govern(self,govern_name):
        xlk_loc = (By.XPATH,
                   f'//div[@class="cell" and normalize-space()="{govern_name}"]/ancestor::tr//span[@class="el-dropdown-link el-dropdown-selfdefine"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        # 添加数据库步骤
        # 点击资源管理
        self.click(GovernPage.resource_loc)
        # 点击治理中心
        self.click(GovernPage.govern_loc)

        time.sleep(1)
        self.click(xlk_loc)

        self.wait_click(GovernPage.delete_loc)
        self.click(GovernPage.delete_loc)

        self.wait_click(GovernPage.qd_loc)
        self.click(GovernPage.qd_loc)

        element = self.wait(GovernPage.yz_loc)
        if element:
            return self.get_value(GovernPage.yz_loc)