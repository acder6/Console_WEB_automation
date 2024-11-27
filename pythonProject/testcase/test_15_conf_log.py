from base.base_until import BaseUntil
from pageobject.conf_log_page import ConfLogPage


class TestConfLog(BaseUntil):
    """配置日志"""

    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    parameter_1_name = "long_query_time"
    xg_1_value = "1"

    parameter_2_name = "slow_query_log"
    xg_2_value = "true"

    log_name = "test_log"

    index_name = "sphereex-dbplusengine-proxy"

    def test_01_xg_m_parameter(self):
        "修改 MySQL 集群参数"
        xg = ConfLogPage(self.driver)
        xg.xg_parameter(TestConfLog.jq_m_name,TestConfLog.parameter_1_name, TestConfLog.parameter_2_name, TestConfLog.xg_1_value, TestConfLog.xg_2_value)

    def test_02_xg_pg_parameter(self):
        "修改 PG 集群参数"
        xg = ConfLogPage(self.driver)
        xg.xg_parameter(TestConfLog.jq_pg_name, TestConfLog.parameter_1_name, TestConfLog.parameter_2_name,
                        TestConfLog.xg_1_value, TestConfLog.xg_2_value)

    def test_03_xg_ora_parameter(self):
        "修改 Oracle 集群参数"
        xg = ConfLogPage(self.driver)
        xg.xg_parameter(TestConfLog.jq_ora_name, TestConfLog.parameter_1_name, TestConfLog.parameter_2_name,
                        TestConfLog.xg_1_value, TestConfLog.xg_2_value)

    def test_04_conf_log_m(self):
        "MySQL 集群日志配置"
        conf = ConfLogPage(self.driver)
        result = conf.conf_log(TestConfLog.jq_m_name, TestConfLog.log_name,TestConfLog.index_name)
        self.assertEqual("配置成功",result)

    def test_05_conf_log_pg(self):
        "PG 集群日志配置"
        conf = ConfLogPage(self.driver)
        result = conf.conf_log(TestConfLog.jq_pg_name, TestConfLog.log_name,TestConfLog.index_name)
        self.assertEqual("配置成功",result)

    def test_05_conf_log_ora(self):
        "Oracle 集群日志配置"
        conf = ConfLogPage(self.driver)
        result = conf.conf_log(TestConfLog.jq_ora_name, TestConfLog.log_name,TestConfLog.index_name)
        self.assertEqual("配置成功",result)