from base.base_until import BaseUntil
from pageobject.cluster_page import ClusterPage


class TestControlCluster(BaseUntil):
    """集群管理"""
    def test_01_xg_m_cluster(self):
        "修改 MySQL 集群"
        xg = ClusterPage(self.driver)
        cluster_name = "test_m"
        mx = "58.210.177.75"
        result = xg.xg_cluster(cluster_name,mx)
        self.assertEqual(mx, result)

    def test_02_del_m_cluster(self):
        "删除 MySQL 集群"
        de = ClusterPage(self.driver)
        cluster_name = "test_m"
        result = de.del_cluster(cluster_name)

        self.assertEqual("删除成功",result)

    def test_03_xg_pg_cluster(self):
        "修改 PostgreSQL 集群"
        xg = ClusterPage(self.driver)
        cluster_name = "test_pg"
        mx = "58.210.177.75"
        result = xg.xg_cluster(cluster_name,mx)
        self.assertEqual(mx, result)

    def test_04_del_pg_cluster(self):
        "删除 PostgreSQL 集群"
        de = ClusterPage(self.driver)
        cluster_name = "test_pg"
        result = de.del_cluster(cluster_name)

        self.assertEqual("删除成功",result)

    def test_05_xg_ora_cluster(self):
        "修改 Oracle 集群"
        xg = ClusterPage(self.driver)
        cluster_name = "test_ora"
        mx = "58.210.177.75"
        result = xg.xg_cluster(cluster_name,mx)
        self.assertEqual(mx, result)

    def test_06_del_ora_cluster(self):
        "删除 Oracle 集群"
        de = ClusterPage(self.driver)
        cluster_name = "test_ora"
        result = de.del_cluster(cluster_name)

        self.assertEqual("删除成功",result)

    def test_07_add_m_cluster(self):
        "添加 MySQL 集群"
        ad = ClusterPage(self.driver)
        ad.register_m_cluster("test_m", "58.210.177.75", "3308", "root", "root")

    def test_08_add_pg_cluster(self):
        "添加 PostgreSQL 集群"
        ad = ClusterPage(self.driver)
        ad.register_pg_cluster("test_pg", "58.210.177.75", "3313", "root", "root")

    def test_09_add_ora_cluster(self):
        "添加 Oracle 集群"
        ad = ClusterPage(self.driver)
        ad.register_ora_cluster("test_ora", "58.210.177.75", "3309", "root", "root")