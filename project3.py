import mysql.connector as db
class DBHelper:
    def __init__(self):
        #step1 create connection with database
        self.connection = db.connect(user='root',
                                 password='daman@1313',
                                 host= '127.0.0.1',
                                 database='mydatabase')

        #step2 obtain cursor to perform sql operation
        self.cursor = self.connection.cursor()
        print("[DBHelper] connection created and cursor obtained...")

   # insert update and delete write into database

    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL..",sql)
        #step3 execute sql command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL statement executed...")
# select operation
    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL..",sql)
        #step3 execute sql command
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows


