import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage


class JmColumnSuff(BasePage):
    sen_data_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="系统配置"]')

    jmsuff_loc = (By.XPATH, '//li[@class="el-menu-item" and .="加密衍生列名称"]')

    mw_loc = (By.XPATH, '//input[@placeholder="密文列后缀" ]')

    like_loc = (By.XPATH, '//input[@placeholder="模糊列查询后缀"]')

    order_loc = (By.XPATH, '//input[@placeholder="排序列查询后缀"]')

    qr_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "确认更改")]')

    mr_button_loc = (By.XPATH, '//button[@class="el-button el-button--primary" and contains(., "使用默认配置")]')

    yz_loc = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')

    def xg_jm_column_suff(self,mw,like,order):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(JmColumnSuff.sen_data_loc)

        self.click(JmColumnSuff.jmsuff_loc)

        self.clear(JmColumnSuff.mw_loc)
        self.set_keys(JmColumnSuff.mw_loc,mw)

        self.clear(JmColumnSuff.like_loc)
        self.set_keys(JmColumnSuff.like_loc,like)

        self.clear(JmColumnSuff.order_loc)
        self.set_keys(JmColumnSuff.order_loc,order)

        self.click(JmColumnSuff.qr_button_loc)

        self.sx()

        time.sleep(1)
        element = self.wait(JmColumnSuff.mw_loc)
        if element:
            mw_result = self.get_bx_value(JmColumnSuff.mw_loc)
            like_result = self.get_bx_value(JmColumnSuff.like_loc)
            order_result = self.get_bx_value(JmColumnSuff.order_loc)
            return mw_result == mw and like_result == like and order_result == order

    def mr_jm_column_suff(self):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.click(JmColumnSuff.sen_data_loc)

        self.click(JmColumnSuff.jmsuff_loc)

        self.click(JmColumnSuff.mr_button_loc)

        self.sx()

        element = self.wait(JmColumnSuff.mw_loc)
        if element:
            mw_result = self.get_bx_value(JmColumnSuff.mw_loc)
            like_result = self.get_bx_value(JmColumnSuff.like_loc)
            order_result = self.get_bx_value(JmColumnSuff.order_loc)
            return mw_result == "_cipher" and like_result == "_like" and order_result == "_order"