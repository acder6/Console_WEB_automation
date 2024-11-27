
from selenium.webdriver.common.by import By

from base.base_until import BaseUntil
from pageobject.database_page import DatabasePage



class TestAdb(BaseUntil):
    """添加数据库"""

    def test_01_add_m_database(self):
        "添加 MySQL 数据库"
        adp = DatabasePage(self.driver)
        adp.add_m_database("58.210.177.75", "13301", "root", "sphereEx@2021")

    def test_02_add_pg_database(self):

        "添加 PostgreSQL 数据库"
        adp = DatabasePage(self.driver)
        adp.add_pg_database("58.210.177.75", "55555", "wsm", "wsm","wsm")

    def test_03_add_ora_database(self):

        "添加 Oracle数据库"
        adp = DatabasePage(self.driver)
        adp.add_ora_database("192.168.10.20", "1521","helowin", "system", "oracle")
