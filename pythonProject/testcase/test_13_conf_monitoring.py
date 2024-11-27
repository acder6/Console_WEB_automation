from base.base_until import BaseUntil
from pageobject.either_monitoring_page import EitherMonitoringPage


class TestConfMonitoring(BaseUntil):
    """配置监控"""

    host_ip = "58.210.177.75"
    host_label = "58.210.177.75:9100"

    database_name = "MySQL"
    database_label = "58.210.177.75:9104"

    cluster_m_name = "test_m"
    cluster_pg_name = "test_pg"
    cluster_ora_name = "test_ora"

    cluster_m_label = "58.210.177.75:19090"
    cluster_pg_label = "58.210.177.75:19091"
    cluster_ora_label = "58.210.177.75:19092"

    monitoring_addr = "58.210.177.75:9090"
    def test_01_conf_host_monitoring(self):
        "主机配置监控"
        host = EitherMonitoringPage(self.driver)
        result = host.conf_monitoring_host(TestConfMonitoring.host_ip,TestConfMonitoring.monitoring_addr,TestConfMonitoring.host_label)
        self.assertEqual("配置成功",result)

    def test_02_conf_database_monitoring(self):
        "MySQL 数据库配置监控"
        database = EitherMonitoringPage(self.driver)
        database.conf_monitoring_database(TestConfMonitoring.database_name,TestConfMonitoring.monitoring_addr,TestConfMonitoring.database_label)

    def test_03_conf_cluster_m_monitoring(self):
        "MySQL 集群配置监控"
        cluster = EitherMonitoringPage(self.driver)
        result = cluster.conf_monitoring_cluster(TestConfMonitoring.cluster_m_name,TestConfMonitoring.cluster_m_label)
        self.assertEqual("配置成功",result)


    def test_04_conf_cluster_pg_monitoring(self):
        "PG 集群配置监控"
        cluster = EitherMonitoringPage(self.driver)
        result = cluster.conf_monitoring_cluster(TestConfMonitoring.cluster_pg_name,TestConfMonitoring.cluster_pg_label)
        self.assertEqual("配置成功",result)


    def test_05_conf_cluster_ora_monitoring(self):
        "Oracle 集群配置监控"
        cluster = EitherMonitoringPage(self.driver)
        result = cluster.conf_monitoring_cluster(TestConfMonitoring.cluster_ora_name,TestConfMonitoring.cluster_ora_label)
        self.assertEqual("配置成功",result)
