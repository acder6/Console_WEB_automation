from base.base_until import BaseUntil
from pageobject.sql_management_routing import SqlManagementRouting


class TestSqlManagementRouting(BaseUntil):
    """SQL 管理 路由"""
    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    logical_name = "test_04"

    sql_state = "select * from t_mask"

    node_name = "test_0909"

    def test_01_sql_routing_mysql(self):
        "MySQL 集群逻辑库路由"
        rou = SqlManagementRouting(self.driver)
        result = rou.sql_routing(TestSqlManagementRouting.jq_m_name, TestSqlManagementRouting.logical_name, TestSqlManagementRouting.sql_state.upper())
        self.assertEqual(TestSqlManagementRouting.node_name,result)

    def test_02_sql_routing_pg(self):
        "PG 集群逻辑库路由"
        rou = SqlManagementRouting(self.driver)
        result = rou.sql_routing(TestSqlManagementRouting.jq_pg_name, TestSqlManagementRouting.logical_name, TestSqlManagementRouting.sql_state.upper())
        self.assertEqual(TestSqlManagementRouting.node_name,result)


    def test_03_sql_routing_ora(self):
        "Oracle 集群逻辑库路由"
        rou = SqlManagementRouting(self.driver)
        result = rou.sql_routing(TestSqlManagementRouting.jq_ora_name, TestSqlManagementRouting.logical_name, TestSqlManagementRouting.sql_state.upper())
        self.assertEqual(TestSqlManagementRouting.node_name,result)