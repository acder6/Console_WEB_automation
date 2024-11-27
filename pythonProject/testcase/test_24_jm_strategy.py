from base.base_until import BaseUntil
from pageobject.jm_starategy_page import JmStrategyPage


class TestJmStrategy(BaseUntil):
    """内置加密策略"""
    add_name = "test_0829"
    add_type = "AES"

    xg_name = "test_0829"
    xg_type = "DES"

    del_name = "test_0829"
    def test_01_add_jm_strategy(self):
        "添加内置加密策略"
        ad = JmStrategyPage(self.driver)
        result = ad.add_jm_strategy(TestJmStrategy.add_name,TestJmStrategy.add_type)
        self.assertEqual("新增成功",result)

    def test_02_either_jm_strategy(self):
        "编辑内置加密策略"
        eit = JmStrategyPage(self.driver)
        result = (eit.either_jm_strategy(TestJmStrategy.add_name,TestJmStrategy.xg_name,TestJmStrategy.xg_type))
        self.assertEqual(TestJmStrategy.xg_type,result)

    def test_03_del_jm_strategy(self):
        "删除内置加密策略"
        del_jm = JmStrategyPage(self.driver)
        result = del_jm.delete_jm_strategy(TestJmStrategy.del_name)
        self.assertEqual("删除成功",result)
