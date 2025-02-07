import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class ParameterPage(BasePage):
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')


    cluster_parameter_loc = (By.ID, 'tab-third')

    value_loc = (By.XPATH, '//label[@for="value"]//following-sibling::div//input[@class="el-input__inner"]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确 定")]')

    def xg_parameter(self,jq_name,para_name,value):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        xg_loc_para = (By.XPATH,f'//div[@class="cell" and normalize-space()="{para_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        para_yz_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{para_name}"]/ancestor::tr//td[3]/div[@class="cell"]')
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ParameterPage.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ParameterPage.cluster_parameter_loc)

        self.wait(xg_loc_para)
        self.click(xg_loc_para)

        self.set_keys(ParameterPage.value_loc,value)

        self.click(ParameterPage.qd_button_loc)

        time.sleep(2)
        element = self.wait(para_yz_loc)
        if element:
            return self.get_value(para_yz_loc)

    def re_parameter(self,jq_name,para_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        reset_loc_para = (By.XPATH,f'//div[@class="cell" and normalize-space()="{para_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "重置")]')
        para_yz_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{para_name}"]/ancestor::tr//td[3]/div[@class="cell"]')
        mr_para_yz_loc = (By.XPATH, f'//div[@class="cell" and normalize-space()="{para_name}"]/ancestor::tr//td[2]/div[@class="cell"]')

        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ParameterPage.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ParameterPage.cluster_parameter_loc)

        self.wait(reset_loc_para)
        self.click(reset_loc_para)

        self.click(ParameterPage.qd_button_loc)

        time.sleep(2)
        result_mr = self.get_value(mr_para_yz_loc)
        result_yz = self.get_value(para_yz_loc)
        return result_mr == result_yz

