import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage
class TmStrategyPage(BasePage):
    sen_data_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="系统配置"]')

    tm_loc = (By.XPATH, '//li[@class="el-menu-item" and .="内置脱敏策略"]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    name_loc = (By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    type_loc = (By.XPATH, '//label[@for="type"]//following-sibling::div//input[@class="el-input__inner"]')

    type_xz_loc = (By.XPATH,'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="MD5"]')

    price_loc = (By.XPATH, '//label[@for="salt"]//following-sibling::div//input[@class="el-input__inner"]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确 定")]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')
    def add_tm_strategy(self,name,price):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(TmStrategyPage.sen_data_loc)


        self.wait_click(TmStrategyPage.tm_loc)
        self.click(TmStrategyPage.tm_loc)

        time.sleep(1)
        self.click(TmStrategyPage.register_button_loc)

        self.set_keys(TmStrategyPage.name_loc,name)

        self.wait(TmStrategyPage.type_loc)
        self.wait_click(TmStrategyPage.type_loc)
        self.click(TmStrategyPage.type_loc)

        self.click(TmStrategyPage.type_xz_loc)

        self.set_keys(TmStrategyPage.price_loc,price)

        self.wait_click(TmStrategyPage.qd_button_loc)
        self.click(TmStrategyPage.qd_button_loc)

        element = self.wait(TmStrategyPage.yz_loc)
        if element:
            return self.get_value(TmStrategyPage.yz_loc)

    def either_rule(self, name, xg_name, price):
        either_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "编辑")]')

        yz_mx_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{xg_name}"]/ancestor::tr/td[3]/div[@class="cell"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(TmStrategyPage.sen_data_loc)
        self.click(TmStrategyPage.sen_data_loc)

        self.click(TmStrategyPage.tm_loc)

        self.wait(either_loc)
        self.wait_click(either_loc)
        self.click(either_loc)

        self.clear(TmStrategyPage.name_loc)
        self.set_keys(TmStrategyPage.name_loc, xg_name)

        self.clear(TmStrategyPage.price_loc)
        self.set_keys(TmStrategyPage.price_loc, price)

        self.click(TmStrategyPage.qd_button_loc)

        time.sleep(1)
        element = self.wait(yz_mx_loc)
        if element:
            return self.get_number_value(yz_mx_loc)

    def del_rule(self, name):
        del_loc = (By.XPATH,
                   f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(TmStrategyPage.sen_data_loc)
        self.click(TmStrategyPage.sen_data_loc)

        self.click(TmStrategyPage.tm_loc)

        self.wait(del_loc)
        self.wait_click(del_loc)
        self.click(del_loc)

        self.wait(TmStrategyPage.qr_loc)
        self.click(TmStrategyPage.qr_loc)

        element = self.wait(TmStrategyPage.yz_loc)
        if element:
            return self.get_value(TmStrategyPage.yz_loc)
