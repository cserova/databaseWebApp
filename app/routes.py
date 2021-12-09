from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import QueryForm
from app.database import get_mysql_connection, get_redshift_connection, get_mongodb_connection
from app.aws_credentials import *
import json
import re
from psycopg2.extensions import adapt
from psycopg2 import OperationalError

@app.route('/index', methods=['GET'])
def index():
    form = QueryForm()
    return render_template('index.html', form=form)

@app.route('/results/mysql/<database>', methods=['POST'])
def get_results_from_mysql(database):
    mysql_db_host = ""
    if 'adni' in database:
        mysql_db_host = mysql_adnidb_host
    else:
        mysql_db_host = mysql_host
    mysql_connection = get_mysql_connection(
        host=mysql_db_host,
        user=mysql_user,
        password=mysql_password,
        db=database,
        port=mysql_port
    )
    return runQueryAndReturnResult(mysql_connection, str(request.data), fetch_all = True)

@app.route('/results/redshift/<database>', methods=['POST'])
def get_results_from_redshift(database):
    redshift_connection = get_redshift_connection(
        host=rs_host,
        user=rs_user,
        password=rs_password,
        dbname=database.lower(),
        port=rs_port
    )
    return runQueryAndReturnResult(redshift_connection, str(request.data), fetch_all = True)

@app.route('/results/mongoDb/<database>', methods=['POST'])
def get_results_from_mongodb(database):
    redshift_connection = get_mongodb_connection(
        driver=mongodb_odbc_driver,
        host=mongodb_host,
        db=database,
        port=mongodb_port
    )
    return runQueryAndReturnResult(redshift_connection, str(request.data), fetch_all = False)

def buildQueryFromInput(raw_query):
    trimmed_query = re.sub('\\\\"', '"', raw_query[2:-1])
    print(trimmed_query)
    query = re.sub('\s+', ' ', trimmed_query)
    return query

def runQueryAndReturnResult(connection, raw_query, fetch_all):
    query = buildQueryFromInput(raw_query)
    try:
        column_names, results, query_time = connection.run_query(query, fetch_all)
        columns, tabulator_data = createTabulatorTableDataFromResult(column_names, results)
        query_result = [columns, tabulator_data, query_time]
        success = True
    except (Exception, OperationalError) as e:
        success = False
        query_result = str(e)
        print(query_result)
    connection.close()
    return json.dumps([success, query_result])

def createTabulatorTableDataFromResult(column_names, results):
    columns=list(map(lambda column: {"title": column, "field": column}, column_names))
    tabulator_data = []
    for index, row in enumerate(results):
      tabulator_row = {}
      tabulator_row["id"] = index+1
      for i, column in enumerate(column_names):
        tabulator_row[column]=row[i]
      tabulator_data.append(tabulator_row)
    return columns, tabulator_data
