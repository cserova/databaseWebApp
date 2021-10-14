from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import QueryForm
from app.database import get_mysql_connection, get_redshift_connection
from app.aws_credentials import *
import json
import re

#@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    form = QueryForm()
    return render_template('index.html', form=form)

@app.route('/results/mysql/<database>', methods=['POST'])
def get_results_from_mysql(database):
    mysql_connection = get_mysql_connection(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        db=database,
        port=mysql_port
    )
    return runQueryAndReturnResult(mysql_connection, str(request.data))

@app.route('/results/redshift/<database>', methods=['POST'])
def get_results_from_redshift(database):
    redshift_connection = get_redshift_connection(
        host=rs_host,
        user=rs_user,
        password=rs_password,
        dbname=database,
        port=rs_port
    )
    return runQueryAndReturnResult(redshift_connection, str(request.data))

def buildQueryFromInput(raw_query):
    trimmed_query = raw_query[3:-2]
    query = re.sub('\s+', ' ', trimmed_query)
    return query

def runQueryAndReturnResult(connection, raw_query):
    query = buildQueryFromInput(raw_query)
    try:
        column_names, results, query_time = connection.run_query(query)
        columns, tabulator_data = createTabulatorTableDataFromResult(column_names, results)
        query_result = [columns, tabulator_data, query_time]
        success = True
    except Exception as e:
        success = False
        query_result = str(e)
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
