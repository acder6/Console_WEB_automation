import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class RulePage(BasePage):
    sen_data_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="敏感数据识别"]')

    rule_loc = (By.XPATH, '//li[@class="el-menu-item" and .="规则管理"]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    name_loc = (By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    rules_loc = (By.XPATH, '//textarea[@placeholder="请输入正则表达式"]')

    mx_loc = (By.XPATH, '//textarea[@placeholder="请输入内容"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')


    def add_rule(self,name,rules,mx):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RulePage.sen_data_loc)
        self.click(RulePage.sen_data_loc)

        self.click(RulePage.rule_loc)

        self.click(RulePage.register_button_loc)

        self.set_keys(RulePage.name_loc, name)

        self.set_keys(RulePage.rules_loc, rules)

        self.set_keys(RulePage.mx_loc, mx)

        self.click(RulePage.register_button_loc)

        element = self.wait(RulePage.yz_loc)
        if element:
            return self.get_value(RulePage.yz_loc)

    def either_rule(self,name,xg_name,rules,mx):
        either_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "编辑")]')

        yz_mx_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{xg_name}"]/ancestor::tr/td[3]/div[@class="cell"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RulePage.sen_data_loc)
        self.click(RulePage.sen_data_loc)

        self.click(RulePage.rule_loc)

        self.wait(either_loc)
        self.wait_click(either_loc)
        self.click(either_loc)

        self.clear(RulePage.name_loc)
        self.set_keys(RulePage.name_loc, xg_name)

        self.clear(RulePage.rules_loc)
        self.set_keys(RulePage.rules_loc, rules)

        self.clear(RulePage.mx_loc)
        self.set_keys(RulePage.mx_loc, mx)

        self.click(RulePage.register_button_loc)


        time.sleep(1)
        element = self.wait(yz_mx_loc)
        if element:
            return self.get_value(yz_mx_loc)


    def del_rule(self,name):
        del_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button del el-button--text" and contains(., "删除")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RulePage.sen_data_loc)
        self.click(RulePage.sen_data_loc)

        self.click(RulePage.rule_loc)

        self.wait(del_loc)
        self.wait_click(del_loc)
        self.click(del_loc)


        self.wait(RulePage.qr_loc)
        self.click(RulePage.qr_loc)

        element = self.wait(RulePage.yz_loc)
        if element:
            return self.get_value(RulePage.yz_loc)
