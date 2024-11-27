from base.base_until import BaseUntil
from pageobject.cluster_logical import ClusterLogical


class TestLogical(BaseUntil):
    """集群逻辑库"""

    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    logical_name = "test_04"

    def test_01_add_logical_mysql(self):
        "添加 MySQL 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功",result)

    def test_02_add_node_logical_mysql(self):
        "MySQL 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)


    def test_03_del_node_logical_mysql(self):
        "MySQL 集群逻辑库 删除节点"
        delt = ClusterLogical(self.driver)
        result = delt.del_node_database(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)


    def test_04_del_logical_mysql(self):
        "删除 MySQL 集群逻辑库"
        delt = ClusterLogical(self.driver)
        result = delt.del_cluster_logical(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("删除成功",result)




    def test_05_add_logical_pg(self):
        "添加 PG 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功",result)


    def test_06_add_node_logical_pg(self):
        "PG 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)


    def test_07_del_node_logical_pg(self):
        "PG 集群逻辑库 删除节点"
        delt = ClusterLogical(self.driver)
        result = delt.del_node_database(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)

    def test_08_del_logical_pg(self):
        "删除 PG 集群逻辑库"
        delt = ClusterLogical(self.driver)
        result = delt.del_cluster_logical(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("删除成功",result)


    def test_09_add_logical_ora(self):
        "添加 Oracle 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功",result)

    def test_10_add_node_logical_ora(self):
        "Oracle 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)


    def test_11_del_node_logical_ora(self):
        "Oracle 集群逻辑库 删除节点"
        delt = ClusterLogical(self.driver)
        result = delt.del_node_database(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)

    def test_12_del_logical_ora(self):
        "删除 Oracle 集群逻辑库"
        delt = ClusterLogical(self.driver)
        result = delt.del_cluster_logical(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("删除成功",result)

    def test_13_add_logical_mysql(self):
        "添加 MySQL 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功", result)

    def test_14_add_node_logical_mysql(self):
        "MySQL 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_m_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功", result)

    def test_15_add_logical_pg(self):
        "添加 PG 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功", result)

    def test_16_add_node_logical_pg(self):
        "PG 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_pg_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功", result)

    def test_17_add_logical_ora(self):
        "添加 Oracle 集群逻辑库"
        ad = ClusterLogical(self.driver)
        result = ad.add_cluster_logical(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("新建逻辑库成功",result)

    def test_18_add_node_logical_ora(self):
        "Oracle 集群逻辑库 添加节点"
        ad_node = ClusterLogical(self.driver)
        result = ad_node.add_node_database(TestLogical.jq_ora_name, TestLogical.logical_name)
        self.assertEqual("配置更新成功",result)