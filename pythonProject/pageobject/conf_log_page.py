import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage



class ConfLogPage(BasePage):
    cluster_loc = (By.XPATH, '//li[@class="el-menu-item submenu-title-noDropdown" and .="集群管理"]')

    cluster_parameter_loc = (By.ID, 'tab-third')

    cluster_log_loc = (By.ID, 'tab-sxith')

    value_loc = (By.XPATH, '//label[@for="value"]//following-sibling::div//input[@class="el-input__inner"]')

    qd_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确 定")]')

    # 日志中心名称下拉框
    addr_log_xlk_loc = (By.XPATH,
                         '//label[@for="logCenter"]//following-sibling::div//input[@class="el-input__inner" and @readonly="readonly"]')

    # 索引名称
    label_moni_loc = (By.XPATH, '//label[@for="logIndex"]//following-sibling::div//input[@class="el-input__inner"]')

    # 确定按钮
    qd_loc = (By.XPATH,'//button[@class="el-button el-button--primary" and normalize-space(.//span)="确 定"]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')


    def xg_parameter(self,jq_name,para_1_name,para_2_name,value_1,value_2):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        xg_1_loc_para = (By.XPATH,f'//div[@class="cell" and normalize-space()="{para_1_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        xg_2_loc_para = (By.XPATH,f'//div[@class="cell" and normalize-space()="{para_2_name}"]/ancestor::tr//button[@class="el-button el-button--text" and contains(., "修改")]')
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ConfLogPage.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ConfLogPage.cluster_parameter_loc)

        self.wait(xg_1_loc_para)
        self.click(xg_1_loc_para)

        self.set_keys(ConfLogPage.value_loc,value_1)

        self.click(ConfLogPage.qd_button_loc)

        time.sleep(2)
        self.wait(xg_2_loc_para)
        self.click(xg_2_loc_para)

        self.set_keys(ConfLogPage.value_loc, value_2)

        self.click(ConfLogPage.qd_button_loc)


    def conf_log(self,jq_name,log_name,index_name):
        jq_loc = (By.XPATH, f'//button[@class="el-button el-button--text" and ./span[contains(text(), "{jq_name}")]]')
        # 日志中心名称
        name_log_loc = (By.XPATH,
                         f'//ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item" and .//span="{log_name}"]')
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(ConfLogPage.cluster_loc)

        time.sleep(1)
        self.wait(jq_loc)
        self.click(jq_loc)

        self.click(ConfLogPage.cluster_log_loc)

        self.wait_click(ConfLogPage.addr_log_xlk_loc)
        self.click(ConfLogPage.addr_log_xlk_loc)

        self.wait(name_log_loc)
        self.click(name_log_loc)

        self.set_keys(ConfLogPage.label_moni_loc,index_name)

        self.click(ConfLogPage.qd_loc)

        element = self.wait(ConfLogPage.yz_loc)
        if element:
            return self.get_value(ConfLogPage.yz_loc)

