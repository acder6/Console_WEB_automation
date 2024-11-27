from base.base_until import BaseUntil
from pageobject.monitoring_page import MonitoringPage


class TestMonitoring(BaseUntil):
    """监控中心"""

    addr = "58.210.177.75"
    port = "9090"
    name = "test_monitoring"

    xg_mx = "测试监控中心"

    def test_01_register_monitoring(self):
        "注册监控中心"
        reg = MonitoringPage(self.driver)
        result = reg.register_monitoring(TestMonitoring.addr,TestMonitoring.port,TestMonitoring.name)

        self.assertEqual("注册成功",result)

    def test_02_th_monitoring(self):
        "探活监控中心"
        th = MonitoringPage(self.driver)
        result = th.th_monitoring(TestMonitoring.name)
        self.assertEqual("探活成功",result)

    def test_03_xg_monitoring(self):
        "修改监控中心信息"
        xg = MonitoringPage(self.driver)
        result = xg.xg_monitoring(TestMonitoring.name,TestMonitoring.xg_mx)
        self.assertEqual(TestMonitoring.xg_mx,result)

    def test_04_delete_monitoring(self):
        "删除监控中心"
        delete = MonitoringPage(self.driver)
        result = delete.delete_monitoring(TestMonitoring.name)
        self.assertEqual("删除成功",result)


    def test_05_register_monitoring(self):
        "注册监控中心"
        reg = MonitoringPage(self.driver)
        result = reg.register_monitoring(TestMonitoring.addr, TestMonitoring.port, TestMonitoring.name)

        self.assertEqual("注册成功", result)



