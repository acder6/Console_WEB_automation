from base.base_until import BaseUntil
from pageobject.cluster_storage_node import ClusterStorageNode


class TestStorageNode(BaseUntil):
    """注册存储节点"""

    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    m_db_name = "test_0902"
    pg_db_name = "wsm"

    m_node_name = "test_0909"
    pg_node_name = "test_0909"
    ora_node_name = "test_0909"

    def test_01_add_m_storage_node(self):

        "注册 MySQL 存储节点"
        ad = ClusterStorageNode(self.driver)
        result = ad.add_m_storage_node(TestStorageNode.jq_m_name,TestStorageNode.m_db_name,TestStorageNode.m_node_name)

        self.assertEqual("注册存储节点成功",result)

    def test_02_add_pg_storage_node(self):
        "注册 PostgreSQL 存储节点"
        adp = ClusterStorageNode(self.driver)
        result = adp.add_pg_storage_node(TestStorageNode.jq_pg_name,TestStorageNode.pg_node_name)
        self.assertEqual("注册存储节点成功", result)

    def test_03_add_ora_storage_node(self):
        "注册 Oracle 存储节点"
        adp = ClusterStorageNode(self.driver)
        result = adp.add_ora_storage_node(TestStorageNode.jq_ora_name,TestStorageNode.pg_node_name)
        self.assertEqual("注册存储节点成功", result)
