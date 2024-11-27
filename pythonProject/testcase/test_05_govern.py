from base.base_until import BaseUntil
from pageobject.govern_page import GovernPage


class TestGovern(BaseUntil):
    """治理中心"""

    govern_name = "test_0903"
    addr = "58.210.177.75:2181"

    xg_mx = "修改治理中心"
    def test_01_register_govern(self):
        "注册治理中心"
        red = GovernPage(self.driver)
        result = red.register_govern(TestGovern.govern_name, TestGovern.addr)
        self.assertEqual("注册治理中心成功", result)

    def test_02_xg_govern(self):
        "修改治理中心"
        xg = GovernPage(self.driver)
        result = xg.xg_govern(TestGovern.govern_name, TestGovern.xg_mx)
        self.assertEqual(TestGovern.xg_mx, result)

    def test_03_eith_node_govern(self):
        "治理中心节点"
        eith = GovernPage(self.driver)
        result = eith.eith_node(TestGovern.govern_name)
        self.assertEqual("探活成功", result)

    def test_04_delete_govern(self):
        "删除治理中心"
        delete = GovernPage(self.driver)
        result = delete.delete_govern(TestGovern.govern_name)
        self.assertEqual("删除成功", result)

    def test_05_register_govern(self):
        "注册治理中心"
        red = GovernPage(self.driver)
        result = red.register_govern(TestGovern.govern_name, TestGovern.addr)
        self.assertEqual("注册治理中心成功", result)