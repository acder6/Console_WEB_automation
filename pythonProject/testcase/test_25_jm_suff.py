
from base.base_until import BaseUntil
from pageobject.jm_column_suff import JmColumnSuff


class TestJmSuff(BaseUntil):
    """加密衍生列后缀"""

    def test_01_xg_jm_column_suff(self):
        "更改后缀"
        mw = "abc"
        like = "abc"
        order = "abc"
        xg = JmColumnSuff(self.driver)

        result = xg.xg_jm_column_suff(mw,like,order)

        self.assertTrue(result)

    def test_02_mr_jm_column_suff(self):
        "使用默认配置"
        mr = JmColumnSuff(self.driver)
        result = mr.mr_jm_column_suff()
        self.assertTrue(result)