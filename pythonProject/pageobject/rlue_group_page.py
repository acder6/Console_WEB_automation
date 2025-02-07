import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class RuleGroupPage(BasePage):
    sen_data_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="敏感数据识别"]')

    rule_loc = (By.XPATH, '//li[@class="el-menu-item" and .="规则管理"]')

    rule_grop_loc = (By.ID, 'tab-ruleGroup')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    name_loc = (By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    xz_loc = (By.XPATH,'//label[@class="el-checkbox" and contains(., "全部规则")]')

    mx_loc = (By.XPATH, '//textarea[@placeholder="请输入内容"]')

    yd_loc = (By.XPATH,'//button[@class="el-button el-button--primary el-transfer__button"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')

    def add_group(self,name,mx):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RuleGroupPage.sen_data_loc)
        self.click(RuleGroupPage.sen_data_loc)

        self.click(RuleGroupPage.rule_loc)

        self.click(RuleGroupPage.rule_grop_loc)

        self.click(RuleGroupPage.register_button_loc)

        time.sleep(1)
        self.set_keys(RuleGroupPage.name_loc,name)

        self.set_keys(RuleGroupPage.mx_loc,mx)

        self.wait_click(RuleGroupPage.xz_loc)
        self.click(RuleGroupPage.xz_loc)

        self.wait_click(RuleGroupPage.yd_loc)
        self.click(RuleGroupPage.yd_loc)

        self.click(RuleGroupPage.register_button_loc)

        element = self.wait(RuleGroupPage.yz_loc)
        if element:
            return self.get_value(RuleGroupPage.yz_loc)

    def either_rule(self,name,xg_name,mx):
        either_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "编辑")]')

        yz_mx_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{xg_name}"]/ancestor::tr/td[4]/div[@class="cell"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RuleGroupPage.sen_data_loc)
        self.click(RuleGroupPage.sen_data_loc)

        self.click(RuleGroupPage.rule_loc)

        self.click(RuleGroupPage.rule_grop_loc)

        time.sleep(1)
        self.wait_click(either_loc)
        self.click(either_loc)

        self.clear(RuleGroupPage.name_loc)
        self.set_keys(RuleGroupPage.name_loc, xg_name)

        self.clear(RuleGroupPage.mx_loc)
        self.set_keys(RuleGroupPage.mx_loc, mx)

        self.click(RuleGroupPage.register_button_loc)


        time.sleep(1)
        element = self.wait(yz_mx_loc)
        if element:
            return self.get_value(yz_mx_loc)


    def create_rule(self,name):
        create_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "创建副本")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RuleGroupPage.sen_data_loc)
        self.click(RuleGroupPage.sen_data_loc)

        self.click(RuleGroupPage.rule_loc)

        self.click(RuleGroupPage.rule_grop_loc)

        time.sleep(1)
        self.wait_click(create_loc)
        self.click(create_loc)

        time.sleep(1)
        self.wait_click(RuleGroupPage.register_button_loc)
        self.click(RuleGroupPage.register_button_loc)

        element = self.wait(RuleGroupPage.yz_loc)
        if element:
            return self.get_value(RuleGroupPage.yz_loc)
    def del_rule(self,name):
        del_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button del el-button--text" and contains(., "删除")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(RuleGroupPage.sen_data_loc)
        self.click(RuleGroupPage.sen_data_loc)

        self.click(RuleGroupPage.rule_loc)

        self.click(RuleGroupPage.rule_grop_loc)

        time.sleep(1)
        self.wait_click(del_loc)
        self.click(del_loc)


        self.wait(RuleGroupPage.qr_loc)
        self.click(RuleGroupPage.qr_loc)

        element = self.wait(RuleGroupPage.yz_loc)
        if element:
            return self.get_value(RuleGroupPage.yz_loc)