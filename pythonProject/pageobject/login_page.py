from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):

    #页面元素
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    checkbox_loc = (By.XPATH, '//span[@class="el-checkbox__inner"]')
    submit_loc = (By.XPATH, '//button[@class="el-button el-button--primary"]')
    index_loc = (By.XPATH, '//div[@class="dashboard-mod"]//h3[text()="资源概览"]')

    #页面动作
    def login_ecshop(self, username, password):
        self.set_keys(LoginPage.username_loc,username)
        self.set_keys(LoginPage.password_loc,password)
        self.click(LoginPage.checkbox_loc)
        self.click(LoginPage.submit_loc)

    #断言
    def assert_login(self):
        element=self.wait(LoginPage.index_loc)
        if element:
            return self.get_value(LoginPage.index_loc)