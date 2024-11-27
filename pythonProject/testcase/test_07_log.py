from base.base_until import BaseUntil
from pageobject.log_page import LogPage


class TestLog(BaseUntil):
    """日志中心"""
    addr = "58.210.177.75:9200"
    name = "test_log"

    mx = "测试日志中心"

    def test_01_register_log(self):
        "注册日志中心"
        reg = LogPage(self.driver)
        result = reg.register_Log(TestLog.addr, TestLog.name)

        self.assertEqual("创建成功", result)

    def test_02_eith_node_th_log(self):
        "管理日志中心 --探活"
        th = LogPage(self.driver)
        result = th.eith_node_th_log(TestLog.name)

        self.assertEqual("探活成功", result)

    def test_03_xg_log(self):
        "修改日志中心"
        xg = LogPage(self.driver)
        result = xg.xg_log(TestLog.name, TestLog.mx)
        self.assertEqual(TestLog.mx, result)

    def test_04_delete_log(self):
        "删除日志中心"
        delete = LogPage(self.driver)
        result = delete.delete_monitoring(TestLog.name)
        self.assertEqual("删除成功", result)

    def test_05_register_log(self):
        "注册日志中心"
        reg = LogPage(self.driver)
        result = reg.register_Log(TestLog.addr, TestLog.name)

        self.assertEqual("创建成功", result)