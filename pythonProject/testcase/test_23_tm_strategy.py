from base.base_until import BaseUntil
from pageobject.tm_strategy_page import TmStrategyPage


class TestTmStrategy(BaseUntil):
    """内置脱敏策略"""
    add_name = "test_0829"
    add_price = "15"

    xg_name = "test_0829"
    xg_price = "14"

    del_name = "test_0829"

    def test_01_add_tm_strategy(self):
        "新建脱敏策略"
        ad = TmStrategyPage(self.driver)
        result = ad.add_tm_strategy(TestTmStrategy.add_name, TestTmStrategy.add_price)
        self.assertEqual("新增成功", result)

    def test_02_xg_tm_strategy(self):
        "修改脱敏策略"
        xg = TmStrategyPage(self.driver)
        result = xg.either_rule(TestTmStrategy.add_name, TestTmStrategy.xg_name, TestTmStrategy.xg_price)
        self.assertEqual(TestTmStrategy.xg_price, result)

    def test_03_del_tm_strategy(self):
        "删除脱敏策略"
        de = TmStrategyPage(self.driver)
        result = de.del_rule(TestTmStrategy.del_name)
        self.assertEqual("删除成功!", result)