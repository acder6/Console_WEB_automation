from base.base_until import BaseUntil
from pageobject.host_page import HostPage


class TestHost(BaseUntil):
    """主机"""

    ip = "58.210.177.75"
    username = "root"
    password = "n&iuXQpd^3UUZMHs"
    port = "22"


    host_name = "test_host"
    def test_01_add_host(self):
        "注册主机"
        ah = HostPage(self.driver)
        ah.add_host(TestHost.ip,TestHost.username,TestHost.password,TestHost.port)

    def test_02_xg_host(self):
        "修改主机"
        xg = HostPage(self.driver)
        result = xg.xg_host(TestHost.host_name,TestHost.ip)
        self.assertEqual(TestHost.host_name,result)

    def test_03_delete_host(self):
        "删除主机"
        dh = HostPage(self.driver)
        result = dh.delete_host(TestHost.ip)
        self.assertEqual("删除成功",result)


    def test_04_add_host(self):
        "注册主机"
        ah = HostPage(self.driver)
        ah.add_host(TestHost.ip, TestHost.username, TestHost.password, TestHost.port)