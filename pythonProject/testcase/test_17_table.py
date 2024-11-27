from base.base_until import BaseUntil
from pageobject.logical_table import LogicalTable


class TestTable(BaseUntil):
    """表"""
    table_state = "create table student(id int not null primary key,name varchar(100));"
    table_xg_state = "alter table student add age int;"

    m_db_name = "test_0902"
    pg_db_name = "wsm"
    ora_db_name = "helowin"

    jq_m_name = "test_m"
    jq_pg_name = "test_pg"
    jq_ora_name = "test_ora"

    logical_name = "test_04"

    table_name = "student"

    def test_01_create_table_mysql(self):
        "MySQL 集群逻辑库 新建表"
        cra = LogicalTable(self.driver)
        result = cra.create_table(TestTable.jq_m_name, TestTable.logical_name, TestTable.table_state)
        self.assertEqual("新建成功",result)

    def test_02_xg_table_mysql(self):
        "MySQL 集群逻辑库 修改表"
        xg = LogicalTable(self.driver)
        result = xg.xg_table(TestTable.jq_m_name, TestTable.logical_name, TestTable.table_name, TestTable.table_xg_state)
        self.assertEqual("修改成功",result)


    def test_03_view_table_struct_mysql(self):
        "MySQL 集群逻辑库 查看表结构"
        vs = LogicalTable(self.driver)
        result = vs.view_table_struct(TestTable.jq_m_name, TestTable.logical_name, TestTable.table_name)
        print(result)

    def test_04_view_table_dist_mysql(self):
        "MySQL 集群逻辑库 查看表分布"
        vd = LogicalTable(self.driver)
        result = vd.view_table_dist(TestTable.jq_m_name, TestTable.logical_name, TestTable.table_name)
        self.assertEqual(TestTable.m_db_name,result)

    def test_05_delete_table_mysql(self):
        "MySQL 集群逻辑库 删除表"
        de = LogicalTable(self.driver)
        result = de.delete_table(TestTable.jq_m_name, TestTable.logical_name, TestTable.table_name)
        self.assertEqual("删除成功!",result)

    def test_06_create_table_pg(self):
        "PG 集群逻辑库 新建表"
        cra = LogicalTable(self.driver)
        result = cra.create_table(TestTable.jq_pg_name, TestTable.logical_name, TestTable.table_state)
        self.assertEqual("新建成功",result)

    def test_07_xg_table_pg(self):
        "PG 集群逻辑库 修改表"
        xg = LogicalTable(self.driver)
        result = xg.xg_table(TestTable.jq_pg_name, TestTable.logical_name, TestTable.table_name, TestTable.table_xg_state)
        self.assertEqual("修改成功",result)


    def test_08_view_table_struct_pg(self):
        "PG 集群逻辑库 查看表结构"
        vs = LogicalTable(self.driver)
        result = vs.view_table_struct(TestTable.jq_pg_name, TestTable.logical_name, TestTable.table_name)
        print(result)

    def test_09_view_table_dist_pg(self):
        "PG 集群逻辑库 查看表分布"
        vd = LogicalTable(self.driver)
        result = vd.view_table_dist(TestTable.jq_pg_name, TestTable.logical_name, TestTable.table_name)
        self.assertEqual(TestTable.pg_db_name,result)

    def test_10_delete_table_pg(self):
        "PG 集群逻辑库 删除表"
        de = LogicalTable(self.driver)
        result = de.delete_table(TestTable.jq_pg_name, TestTable.logical_name, TestTable.table_name)
        self.assertEqual("删除成功!",result)

    def test_11_create_table_ora(self):
        "Oracle 集群逻辑库 新建表"
        cra = LogicalTable(self.driver)
        result = cra.create_table(TestTable.jq_ora_name, TestTable.logical_name, TestTable.table_state)
        self.assertEqual("新建成功",result)

    def test_12_xg_table_ora(self):
        "Oracle 集群逻辑库 修改表"
        xg = LogicalTable(self.driver)
        result = xg.xg_table(TestTable.jq_ora_name, TestTable.logical_name, TestTable.table_name.upper(), TestTable.table_xg_state)
        self.assertEqual("修改成功",result)


    def test_13_view_table_struct_ora(self):
        "Oracle 集群逻辑库 查看表结构"
        vs = LogicalTable(self.driver)
        result = vs.view_table_struct(TestTable.jq_ora_name, TestTable.logical_name, TestTable.table_name.upper())
        print(result)

    def test_14_view_table_dist_ora(self):
        "Oracle 集群逻辑库 查看表分布"
        vd = LogicalTable(self.driver)
        result = vd.view_table_dist(TestTable.jq_ora_name, TestTable.logical_name, TestTable.table_name.upper())
        self.assertEqual(TestTable.ora_db_name,result)

    def test_15_delete_table_ora(self):
        "Oracle 集群逻辑库 删除表"
        de = LogicalTable(self.driver)
        result = de.delete_table(TestTable.jq_ora_name, TestTable.logical_name, TestTable.table_name.upper())
        self.assertEqual("删除成功!",result)