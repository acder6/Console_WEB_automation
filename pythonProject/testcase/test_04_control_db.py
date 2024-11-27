from base.base_until import BaseUntil
from pageobject.database_page import DatabasePage


class TestControlDb(BaseUntil):
    """数据库管理"""
    def test_01_th_mysql_database(self):
        "探活 MySQL 数据库"
        th = DatabasePage(self.driver)
        database_name = "MySQL"
        result = th.th_m_database(database_name)

        self.assertEqual("探活成功", result)

    def test_02_xg_mysql_database(self):
        "修改 MySQL 数据库"
        xg = DatabasePage(self.driver)
        database_name = "MySQL"
        expect_ip = "192.168.10.20"
        actual_ip = xg.xg_m_database(database_name,expect_ip)
        self.assertEqual(expect_ip, actual_ip)

    def test_03_delete_database(self):
        "删除 MySQL 数据库"
        sc = DatabasePage(self.driver)
        database_name = "MySQL"
        result = sc.delete_m_database(database_name)
        self.assertEqual("删除成功", result)


    def test_04_th_PostgreSQL_database(self):
        "探活 PostgreSQL 数据库"
        th = DatabasePage(self.driver)
        database_name = "PostgreSQL"
        result = th.th_m_database(database_name)

        self.assertEqual("探活成功", result)

    def test_05_xg_PostgreSQL_database(self):
        "修改 PostgreSQL 数据库"
        xg = DatabasePage(self.driver)
        database_name = "PostgreSQL"
        expect_ip = "192.168.10.20"
        actual_ip = xg.xg_m_database(database_name,expect_ip)
        self.assertEqual(expect_ip, actual_ip)

    def test_06_PostgreSQL_database(self):
        "删除 PostgreSQL 数据库"
        sc = DatabasePage(self.driver)
        database_name = "PostgreSQL"
        result = sc.delete_m_database(database_name)
        self.assertEqual("删除成功", result)

    def test_07_th_Oracle_database(self):
        "探活 Oracle 数据库"
        th = DatabasePage(self.driver)
        database_name = "Oracle"
        result = th.th_m_database(database_name)

        self.assertEqual("探活成功", result)

    def test_08_xg_Oracle_database(self):
        "修改 Oracle 数据库"
        xg = DatabasePage(self.driver)
        database_name = "Oracle"
        expect_ip = "192.168.10.20"
        actual_ip = xg.xg_m_database(database_name,expect_ip)
        self.assertEqual(expect_ip, actual_ip)

    def test_09_Oracle_database(self):
        "删除 Oracle 数据库"
        sc = DatabasePage(self.driver)
        database_name = "Oracle"
        result = sc.delete_m_database(database_name)
        self.assertEqual("删除成功", result)


    def test_10_add_m_database(self):
        "添加 MySQL 数据库"
        adp = DatabasePage(self.driver)
        adp.add_m_database("58.210.177.75", "13301", "root", "sphereEx@2021")

    def test_11_add_pg_database(self):

        "添加 PostgreSQL 数据库"
        adp = DatabasePage(self.driver)
        adp.add_pg_database("58.210.177.75", "55555", "wsm", "wsm","wsm")

    def test_12_add_ora_database(self):

        "添加 Oracle数据库"
        adp = DatabasePage(self.driver)
        adp.add_ora_database("192.168.10.20", "1521","helowin", "system", "oracle")