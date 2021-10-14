import pymysql
import psycopg2
from time import time

class database_connection():
    def run_query(self, query):
        start_time = time()
        self.cursor.execute(query)
        self.db.commit()
        col_info = self.cursor.description
        results = self.cursor.fetchall()
        query_time = str(round((time() - start_time) * 1000, 2)) + " ms"

        col_name = []
        if col_info != None:
            for i in range(len(col_info)):
                col_name.append(col_info[i][0])
        return col_name, results, query_time

    def close(self):
        self.cursor.close()
        self.db.close()

class get_mysql_connection(database_connection):
    def __init__(self, host, user, password, db, port):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=port
        )
        self.cursor = self.db.cursor()

class get_redshift_connection(database_connection):
    def __init__(self, host, user, password, dbname, port):
        self.db = psycopg2.connect(
            host=host,
            dbname=dbname,
            port=port,
            user=user,
            password=password
        )
        self.cursor = self.db.cursor()