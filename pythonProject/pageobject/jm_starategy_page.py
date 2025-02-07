import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class JmStrategyPage(BasePage):
    sen_data_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="系统配置"]')

    jm_loc = (By.XPATH, '//li[@class="el-menu-item" and .="内置加密策略"]')

    register_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')

    name_loc = (By.XPATH, '//label[@for="name"]//following-sibling::div//input[@class="el-input__inner"]')

    type_loc = (By.XPATH, '//label[@for="algorithmType"]//following-sibling::div//input[@class="el-input__inner"]')

    key_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "随机生成")]')

    xz_mw_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "存储明文")]')

    xz_mwf_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "使用明文列查询")]')

    xz_like_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "启用模糊查询")]')

    xz_order_loc = (By.XPATH, '//label[@class="el-checkbox" and contains(., "启用排序查询")]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确定")]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    qr_loc = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "] ')

    def add_jm_strategy(self,name,type1):
        type_xz_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{type1}"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(JmStrategyPage.sen_data_loc)

        self.click(JmStrategyPage.jm_loc)

        time.sleep(1)
        self.click(JmStrategyPage.register_button_loc)

        self.set_keys(JmStrategyPage.name_loc, name)

        self.wait_click(JmStrategyPage.type_loc)
        self.click(JmStrategyPage.type_loc)

        self.click(type_xz_loc)

        self.wait_click(JmStrategyPage.key_loc)
        self.click(JmStrategyPage.key_loc)

        self.click(JmStrategyPage.xz_mw_loc)

        self.wait_click(JmStrategyPage.xz_mwf_loc)
        self.click(JmStrategyPage.xz_mwf_loc)

        self.click(JmStrategyPage.xz_like_loc)

        self.click(JmStrategyPage.xz_order_loc)

        self.click(JmStrategyPage.qd_button_loc)

        element = self.wait(JmStrategyPage.yz_loc)
        if element:
            return self.get_value(JmStrategyPage.yz_loc)

    def either_jm_strategy(self, name,xg_name,type):

        either_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "编辑")]')

        yz_xg_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{xg_name}"]/ancestor::tr/td[2]/div[@class="cell"]')

        type_xg_loc = (By.XPATH,f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{type}"]')
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(JmStrategyPage.sen_data_loc)

        self.click(JmStrategyPage.jm_loc)

        time.sleep(1)
        self.wait_click(either_loc)
        self.click(either_loc)

        self.clear(JmStrategyPage.name_loc)
        self.set_keys(JmStrategyPage.name_loc, name)

        self.click(JmStrategyPage.type_loc)

        self.wait_click(type_xg_loc)
        self.click(type_xg_loc)

        self.click(JmStrategyPage.qd_button_loc)

        time.sleep(2)
        element = self.wait(yz_xg_loc)
        if element:
            return self.get_value(yz_xg_loc)

    def delete_jm_strategy(self,name):

        delete_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{name}"]/ancestor::tr//button[@class="el-button del-operation el-button--text" and contains(., "删除")]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(JmStrategyPage.sen_data_loc)

        self.click(JmStrategyPage.jm_loc)

        time.sleep(1)
        self.wait_click(delete_loc)
        self.click(delete_loc)

        self.wait_click(JmStrategyPage.qr_loc)
        self.click(JmStrategyPage.qr_loc)

        element = self.wait(JmStrategyPage.yz_loc)
        if element:
            return self.get_value(JmStrategyPage.yz_loc)

