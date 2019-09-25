import os
import pymysql
from core.config import config
from core.db_info import get_db_table_info_data


class MySqlDDLBuilder:
    def __init__(self, ip, user, password, db, port=3306, **kwargs):
        self.ip = ip
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.conn = pymysql.connect(
            host=self.ip,
            user=self.user,
            passwd=self.password,
            db=self.db,
            charset='utf8mb4',
            port=self.port
        )

    def get_ddl(self, table):
        with self.conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute("show create table {};".format(table))
            result = cursor.fetchall()
            if result:
                return result[0]['Create Table']
        return None


def output_ddl_sql():
    for db in config():
        name = db.get("name")
        file = open(os.path.join("ddl_export", name + ".sql"), "w", encoding="utf8")
        try:
            ddl_builder = MySqlDDLBuilder(db.get("host"), db.get("user"), db.get("pass"), db.get("db"), db.get("port"))
            table_list = get_db_table_info_data(**db)
            for table in table_list:
                ddl_sql = ddl_builder.get_ddl(table.get("table_name"))
                if ddl_sql:
                    file.write(ddl_sql)
                    file.write("\n\n")
            file.close()
        except Exception as e:
            print("exception {}".format(e))