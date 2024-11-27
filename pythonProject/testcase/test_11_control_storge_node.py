from base.base_until import BaseUntil
from pageobject.cluster_storage_node import ClusterStorageNode


class TestClusterStorageNode(BaseUntil):
    """管理存储节点"""


    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    m_node_name = "test_0909"
    pg_node_name = "test_0909"
    ora_node_name = "test_0909"

    m_db_name = "test_0902"

    xg_m_db_name = "test_0906"
    xg_pg_db_name = "yj"
    def test_01_th_m_storage_node(self):
        "探活 MySQL 存储节点"
        th = ClusterStorageNode(self.driver)
        result = th.th_node_database(TestClusterStorageNode.jq_m_name,TestClusterStorageNode.m_node_name)

        self.assertEqual("探活成功",result)

    def test_02_xg_m_storage_node(self):
        "修改 MySQL 存储节点"
        xg = ClusterStorageNode(self.driver)
        result = xg.xg_node_database(TestClusterStorageNode.jq_m_name,TestClusterStorageNode.m_node_name,TestClusterStorageNode.xg_m_db_name)

        self.assertEqual(TestClusterStorageNode.xg_m_db_name,result)

    def test_03_delete_m_storage_node(self):
        "删除 MySQL 存储节点"
        del_node = ClusterStorageNode(self.driver)
        result = del_node.delete_node_database(TestClusterStorageNode.jq_m_name,TestClusterStorageNode.m_node_name)
        self.assertEqual("删除成功",result)

    def test_04_th_pg_storage_node(self):
        "探活 PostgreSQL 存储节点"
        th = ClusterStorageNode(self.driver)
        result = th.th_node_database(TestClusterStorageNode.jq_pg_name,TestClusterStorageNode.pg_node_name)

        self.assertEqual("探活成功",result)

    def test_05_xg_pg_storage_node(self):
        "修改 PostgreSQL 存储节点"
        xg = ClusterStorageNode(self.driver)
        result = xg.xg_node_database(TestClusterStorageNode.jq_pg_name,TestClusterStorageNode.pg_node_name,TestClusterStorageNode.xg_pg_db_name)

        self.assertEqual(TestClusterStorageNode.xg_pg_db_name,result)

    def test_06_delete_pg_storage_node(self):
        "删除 PostgreSQL 存储节点"
        del_node = ClusterStorageNode(self.driver)
        result = del_node.delete_node_database(TestClusterStorageNode.jq_pg_name,TestClusterStorageNode.pg_node_name)
        self.assertEqual("删除成功",result)


    def test_07_th_ora_storage_node(self):
        "探活 Oracle 存储节点"
        th = ClusterStorageNode(self.driver)
        result = th.th_node_database(TestClusterStorageNode.jq_ora_name,TestClusterStorageNode.ora_node_name)

        self.assertEqual("探活成功",result)


    def test_08_delete_ora_storage_node(self):
        "删除 Oracle 存储节点"
        del_node = ClusterStorageNode(self.driver)
        result = del_node.delete_node_database(TestClusterStorageNode.jq_ora_name,TestClusterStorageNode.ora_node_name)
        self.assertEqual("删除成功",result)


    def test_09_add_m_storage_node(self):

        "注册 MySQL 存储节点"
        ad = ClusterStorageNode(self.driver)
        result = ad.add_m_storage_node(TestClusterStorageNode.jq_m_name,TestClusterStorageNode.m_db_name,TestClusterStorageNode.m_node_name)

        self.assertEqual("注册存储节点成功",result)

    def test_10_add_pg_storage_node(self):
        "注册 PostgreSQL 存储节点"
        adp = ClusterStorageNode(self.driver)
        result = adp.add_pg_storage_node(TestClusterStorageNode.jq_pg_name,TestClusterStorageNode.pg_node_name)
        self.assertEqual("注册存储节点成功", result)

    def test_11_add_ora_storage_node(self):
        "注册 Oracle 存储节点"
        adp = ClusterStorageNode(self.driver)
        result = adp.add_ora_storage_node(TestClusterStorageNode.jq_ora_name,TestClusterStorageNode.pg_node_name)
        self.assertEqual("注册存储节点成功", result)