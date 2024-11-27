from base.base_until import BaseUntil
from pageobject.rlue_group_page import RuleGroupPage


class TestRuleGroup(BaseUntil):
    """规则组"""
    add_name = "test_0829"
    add_mx = "test"

    xg_name = "test_0829"
    xg_mx = "test1"

    del_name = "test_0829"

    def test_01_add_rule_group(self):
        "新增规则组"
        ad = RuleGroupPage(self.driver)
        result = ad.add_group(TestRuleGroup.add_name,TestRuleGroup.add_mx)

        self.assertEqual("新增规则组成功",result)

    def test_02_either_rule_group(self):
        "编辑规则组"
        eit = RuleGroupPage(self.driver)
        result = eit.either_rule(TestRuleGroup.add_name,TestRuleGroup.xg_name,TestRuleGroup.xg_mx)
        self.assertEqual(TestRuleGroup.xg_mx,result)

    def test_03_create_rule_group(self):
        "创建副本"
        cr = RuleGroupPage(self.driver)
        result = cr.create_rule(TestRuleGroup.xg_name)
        self.assertEqual("新增副本规则组成功",result)

    def test_04_del_rule_group(self):
        "删除规则组"
        de = RuleGroupPage(self.driver)
        result = de.del_rule(TestRuleGroup.del_name)
        self.assertEqual("删除成功!",result)
