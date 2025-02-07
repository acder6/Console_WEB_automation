import time

from selenium.webdriver.common.by import By

from base.base_login import BaseLogin
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class ViewMonitoringPage(BasePage):
    monitoring_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="监控"]')

    cluster_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="监控"]//following-sibling::ul//li[@class="el-menu-item" and .="集群"]')

    host_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="监控"]//following-sibling::ul//li[@class="el-menu-item" and .="主机"]')

    database_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="监控"]//following-sibling::ul//li[@class="el-menu-item" and .="数据库"]')

    monitoring_view_loc = (By.XPATH, '//div[@class="el-submenu__title" and ./span="监控"]//following-sibling::ul//li[@class="el-menu-item" and .="监控中心"]')

    value_loc = (By.XPATH, '//p[@class="data-item-value"]')

    def view_monitoring_cluster(self, cluster_name):

        jk_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{cluster_name}"]/ancestor::tr//button[@class="el-button el-button--text" and .="集群监控"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(ViewMonitoringPage.monitoring_loc)
        self.click(ViewMonitoringPage.monitoring_loc)

        self.wait_click(ViewMonitoringPage.cluster_loc)
        self.click(ViewMonitoringPage.cluster_loc)

        time.sleep(1)
        self.click(jk_loc)

        result = self.get_value(ViewMonitoringPage.value_loc)

        return result != ''

    def view_monitoring_host(self, host_ip):

        jk_loc = (By.XPATH,f'//div[@class="cell" and normalize-space()="{host_ip}"]/ancestor::tr//button[@class="el-button el-button--text" and .="监控"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(ViewMonitoringPage.monitoring_loc)
        self.click(ViewMonitoringPage.monitoring_loc)

        self.wait_click(ViewMonitoringPage.host_loc)
        self.click(ViewMonitoringPage.host_loc)

        time.sleep(1)
        self.click(jk_loc)

        time.sleep(1)
        result = self.get_value(ViewMonitoringPage.value_loc)

        return result != ''

    def view_monitoring_db(self, database_port):
        jk_loc = (By.XPATH,
                  f'//div[@class="cell" and normalize-space()="{database_port}"]/ancestor::tr//button[@class="el-button el-button--text"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(ViewMonitoringPage.monitoring_loc)
        self.click(ViewMonitoringPage.monitoring_loc)

        self.click(ViewMonitoringPage.database_loc)

        time.sleep(1)
        self.click(jk_loc)

        result = self.get_value(ViewMonitoringPage.value_loc)

        return result != ''

    def view_monitoring_moni_view(self, monitoring_name):
        jk_loc = (By.XPATH,
                  f'//div[@class="cell" and normalize-space()="{monitoring_name}"]/ancestor::tr//button[@class="el-button el-button--text"]')

        # 登录
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        self.wait_click(ViewMonitoringPage.monitoring_loc)
        self.click(ViewMonitoringPage.monitoring_loc)

        self.click(ViewMonitoringPage.monitoring_view_loc)

        time.sleep(1)
        self.click(jk_loc)

        time.sleep(1)
        self.wait(ViewMonitoringPage.value_loc)
        result = self.get_value(ViewMonitoringPage.value_loc)

        return result != ''