from base.base_login import BaseLogin
from base.base_until import BaseUntil
from pageobject.login_page import LoginPage


class TestLogin(BaseUntil):
    """登录"""

    def test_01_login(self):
        "登录"
        lp = LoginPage(self.driver)
        lp.login_ecshop(BaseLogin.login_name, BaseLogin.login_password)

        #断言
        self.assertEqual('资源概览',lp.assert_login())
        return "登录成功"
