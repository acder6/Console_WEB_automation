from base.base_until import BaseUntil
from pageobject.parameter_page import ParameterPage


class TestParameter(BaseUntil):
    """参数"""
    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    parameter_name = "agent_plugins_enabled"
    xg_value = "false"

    def test_01_xg_m_parameter(self):
        "修改 MySQL 参数"
        xg = ParameterPage(self.driver)
        result = xg.xg_parameter(TestParameter.jq_m_name,TestParameter.parameter_name, TestParameter.xg_value)

        self.assertEqual(TestParameter.xg_value,result)

    def test_02_reset_m_parameter(self):
        "重置 MySQL 参数"
        re = ParameterPage(self.driver)
        result = re.re_parameter(TestParameter.jq_m_name,TestParameter.parameter_name)

        self.assertTrue(result)

    def test_03_xg_pg_parameter(self):
        "修改 PG 参数"
        xg = ParameterPage(self.driver)
        result = xg.xg_parameter(TestParameter.jq_pg_name,TestParameter.parameter_name, TestParameter.xg_value)

        self.assertEqual(TestParameter.xg_value,result)

    def test_04_reset_pg_parameter(self):
        "重置 PG 参数"
        re = ParameterPage(self.driver)
        result = re.re_parameter(TestParameter.jq_pg_name,TestParameter.parameter_name)

        self.assertTrue(result)

    def test_05_xg_ora_parameter(self):
        "修改 ora 参数"
        xg = ParameterPage(self.driver)
        result = xg.xg_parameter(TestParameter.jq_ora_name,TestParameter.parameter_name, TestParameter.xg_value)

        self.assertEqual(TestParameter.xg_value,result)

    def test_06_reset_ora_parameter(self):
        "重置 ora 参数"
        re = ParameterPage(self.driver)
        result = re.re_parameter(TestParameter.jq_ora_name,TestParameter.parameter_name)

        self.assertTrue(result)