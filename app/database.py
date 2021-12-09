import pymysql
import psycopg2
import pyodbc
from time import time

class database_connection():

    def fetch_all_results_at_once(self):
        print('Fetching all results at once')
        return self.cursor.fetchall()

    def fetch_results_incrementally(self):
        print('Fetching results incrementally')
        results = []
        i = 0
        try:
            row = self.cursor.fetchone()
        except:
            pass
        while row and i < 1000:
            results.append(row)
            try:
                row = self.cursor.fetchone()
                i = i + 1
            except:
                pass
        return results

    def run_query(self, query, fetch_all):
        start_time = time()
        self.cursor.execute(query)
        col_info = self.cursor.description
        results = []
        if(fetch_all):
            results = self.fetch_all_results_at_once()
        else:
            results = self.fetch_results_incrementally()
        query_time = str(round((time() - start_time) * 1000, 2)) + " ms"

        col_name = []
        if col_info != None:
            for i in range(len(col_info)):
                col_name.append(col_info[i][0])
        if 'insert' in query or 'create' in query:
            self.db.commit()
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

class get_mongodb_connection(database_connection):
    def __init__(self, driver, host, db, port):
        self.db = pyodbc.connect(
            'Driver=' + driver + ';Server=' + host + '; Port=' + str(port) +';Database=' + db + ';',
            autocommit=True
        )
        self.cursor = self.db.cursor()