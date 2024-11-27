from base.base_until import BaseUntil
from pageobject.rule_page import RulePage


class TestRule(BaseUntil):
    """规则"""

    add_name = "test_0829"
    add_rules = "test"
    add_mx = "test"

    xg_name = "test_0829"
    xg_rules = "test1"
    xg_mx = "test1"

    del_name = "test_0829"
    def test_01_add_rule(self):
        "添加规则"
        ar = RulePage(self.driver)
        result = ar.add_rule(TestRule.add_name,TestRule.add_rules,TestRule.add_mx)
        self.assertEqual("新增规则成功", result)

    def test_02_either_rule(self):
        "编辑规则"
        eit = RulePage(self.driver)
        result = eit.either_rule(TestRule.add_name,TestRule.xg_name,TestRule.xg_rules,TestRule.xg_mx)

        self.assertEqual(TestRule.xg_mx, result)


    def test_03_del_rule(self):
        "删除规则"
        del_name = RulePage(self.driver)
        result = del_name.del_rule(TestRule.del_name)

        self.assertEqual("删除成功!", result)