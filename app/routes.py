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

@app.route('/results/mysql', methods=['POST'])
def get_results_from_mysql():
    query = buildQueryFromInput(str(request.data))
    mysql_connection = get_mysql_connection(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        db='instacart_normalized',
        port=mysql_port
    )
    try:
        column_names, results, query_time = mysql_connection.run_query(query)
    except Exception as e:
        column_names=[]
        results = []
        query_time = e
    mysql_connection.close()
    return json.dumps([column_names, results, query_time])

@app.route('/results/redshift', methods=['POST'])
def get_results_from_redshift():
    query = buildQueryFromInput(str(request.data))
    redshift_connection = get_redshift_connection(
        host=rs_host,
        user=rs_user,
        password=rs_password,
        dbname='instacart_normalized',
        port=rs_port,
        options='-c search_path={schema}'.format(schema='instacart_normalized')
    )
    try:
        column_names, results, query_time = redshift_connection.run_query(query)
    except Exception as e:
        column_names=[]
        results = []
        query_time = e
    redshift_connection.close()
    return json.dumps([column_names, results, query_time])

def buildQueryFromInput(raw_query):
    trimmed_query = raw_query[3:-2]
    query = re.sub('\s+', ' ', trimmed_query)
    return query