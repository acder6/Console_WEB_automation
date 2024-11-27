from base.base_until import BaseUntil
from pageobject.view_monitoring_page import ViewMonitoringPage


class TestViewMonitoring(BaseUntil):
    """观察监控情况"""
    cluster_m_name = "test_m"
    cluster_pg_name = "test_pg"
    cluster_ora_name = "test_ora"

    host_ip = "58.210.177.75"

    database_port = "13301"

    monitoring_name = "test_monitoring"

    def test_01_view_monitoring_cluster_m(self):
        "MySQL 集群监控"
        cluster_m = ViewMonitoringPage(self.driver)
        result = cluster_m.view_monitoring_cluster(TestViewMonitoring.cluster_m_name)
        self.assertTrue(result)

    def test_02_view_monitoring_cluster_pg(self):
        "PostgreSQL 集群监控"
        cluster_m = ViewMonitoringPage(self.driver)
        result = cluster_m.view_monitoring_cluster(TestViewMonitoring.cluster_pg_name)
        self.assertTrue(result)

    def test_03_view_monitoring_cluster_ora(self):
        "Oracle 集群监控"
        cluster_m = ViewMonitoringPage(self.driver)
        result = cluster_m.view_monitoring_cluster(TestViewMonitoring.cluster_ora_name)
        self.assertTrue(result)


    def test_04_view_monitoring_host(self):
        "主机监控"
        host = ViewMonitoringPage(self.driver)
        result = host.view_monitoring_host(TestViewMonitoring.host_ip)
        self.assertTrue(result)


    def test_05_view_monitoring_db(self):
        "数据库监控"
        db = ViewMonitoringPage(self.driver)
        result = db.view_monitoring_db(TestViewMonitoring.database_port)
        self.assertTrue(result)

    def test_06_view_monitoring_moin_view(self):
        "监控视图"
        moin = ViewMonitoringPage(self.driver)
        result = moin.view_monitoring_moni_view(TestViewMonitoring.monitoring_name)
        self.assertTrue(result)