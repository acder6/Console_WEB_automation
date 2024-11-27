from base.base_until import BaseUntil
from pageobject.cluster_page import ClusterPage


class TestAddCluster(BaseUntil):
    """添加集群"""

    def test_01_add_m_cluster(self):
        "添加 MySQL 集群"
        ad = ClusterPage(self.driver)
        ad.register_m_cluster("test_m","58.210.177.75","3308","root","root")


    def test_02_add_pg_cluster(self):
        "添加 PostgreSQL 集群"
        ad = ClusterPage(self.driver)
        ad.register_pg_cluster("test_pg","58.210.177.75","3313","root","root")

    def test_03_add_ora_cluster(self):
        "添加 Oracle 集群"
        ad = ClusterPage(self.driver)
        ad.register_ora_cluster("test_ora","58.210.177.75","3309","root","root")
