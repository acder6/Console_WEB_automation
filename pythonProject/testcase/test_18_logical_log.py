from base.base_until import BaseUntil
from pageobject.logical_log import  LogicalLog


class TestLogicalLog(BaseUntil):
    """逻辑库内慢日志"""
    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    logical_name = "test_04"

    def test_01_view_logical_log_mysql(self):
        "MySQL 集群逻辑库慢日志查看"
        view = LogicalLog(self.driver)
        result = view.view_logical_log(TestLogicalLog.jq_m_name,TestLogicalLog.logical_name)
        self.assertEqual("DROP", result)

    def test_02_view_logical_log_pg(self):
        "PG 集群逻辑库慢日志查看"
        view = LogicalLog(self.driver)
        result = view.view_logical_log(TestLogicalLog.jq_pg_name,TestLogicalLog.logical_name)
        self.assertEqual("DROP", result)

    def test_03_view_logical_log_ora(self):
        "Oracle 集群逻辑库慢日志查看"
        view = LogicalLog(self.driver)
        result = view.view_logical_log(TestLogicalLog.jq_ora_name,TestLogicalLog.logical_name)
        self.assertEqual("DROP", result)

    def test_04_derive_logical_log_mysql(self):
        "MySQL 集群逻辑库导出慢日志"
        derive = LogicalLog(self.driver)
        result = derive.derive_logical_log(TestLogicalLog.jq_m_name,TestLogicalLog.logical_name)
        self.assertTrue(result)

    def test_05_derive_logical_log_pg(self):
        "PG 集群逻辑库导出慢日志"
        derive = LogicalLog(self.driver)
        result = derive.derive_logical_log(TestLogicalLog.jq_pg_name,TestLogicalLog.logical_name)
        self.assertTrue(result)

    def test_06_derive_logical_log_ora(self):
        "Oracle 集群逻辑库导出慢日志"
        derive = LogicalLog(self.driver)
        result = derive.derive_logical_log(TestLogicalLog.jq_ora_name,TestLogicalLog.logical_name)
        self.assertTrue(result)