from base.base_until import BaseUntil
from pageobject.sql_management_log import SqlManagementLog


class TestsqlManagementLog(BaseUntil):
    """SQL 管理 慢日志"""
    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    logical_name = "test_04"

    sql_type = "alter"

    def test_01_view_sql_management_log_mysql(self):
        "MySQL 集群逻辑库 查看慢日志"
        view = SqlManagementLog(self.driver)
        result = view.view_log(TestsqlManagementLog.jq_m_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())
        self.assertEqual("ALTER",result)

    def test_02_view_sql_management_log_pg(self):
        "PostgreSQL 集群逻辑库 查看慢日志"
        view = SqlManagementLog(self.driver)
        result = view.view_log(TestsqlManagementLog.jq_pg_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())
        self.assertEqual("ALTER", result)

    def test_03_view_sql_management_log_ora(self):
        "Oracle 集群逻辑库 查看慢日志"
        view = SqlManagementLog(self.driver)
        result = view.view_log(TestsqlManagementLog.jq_ora_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())
        self.assertEqual("ALTER",result)


    def test_04_derive_sql_management_log_mysql(self):
        "MySQL 集群逻辑库 导出慢日志"
        derive = SqlManagementLog(self.driver)
        derive.derive_log(TestsqlManagementLog.jq_m_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())

    def test_05_derive_sql_management_log_pg(self):
        "PostgreSQL 集群逻辑库 导出慢日志"
        derive = SqlManagementLog(self.driver)
        derive.derive_log(TestsqlManagementLog.jq_pg_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())


    def test_06_derive_sql_management_log_ora(self):
        "Oracle 集群逻辑库 导出慢日志"
        derive = SqlManagementLog(self.driver)
        derive.derive_log(TestsqlManagementLog.jq_ora_name, TestsqlManagementLog.logical_name,TestsqlManagementLog.sql_type.upper())