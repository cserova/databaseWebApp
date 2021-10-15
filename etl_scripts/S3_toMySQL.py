import pandas as pd
from sqlalchemy import create_engine
import boto3

aws_access_key_id = 'AKIAQ3RV47VWXKYUWAMW'
aws_secret_access_key = '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'

port = 3306
host = 'instacart.c53jriko4hwz.us-east-2.rds.amazonaws.com'
dbname = 'instadb'
user = 'admin'
password = 'TeamDBMS21'

bucket = 'dv-insta-bucket'
files = [
         'aisles.csv',
         'order_products.csv',
         'products.csv',
         'departments.csv',
         'orders.csv'
        ]

connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
sqlEngine = create_engine(connection_string, echo=True)
dbConnection = sqlEngine.connect()

# Push Table one by one
for file_name in files:

    # Connect using aws boto3 library
    s3 = boto3.client('s3',
                      aws_access_key_id = aws_access_key_id,
                      aws_secret_access_key = aws_secret_access_key
                     )

    # Remove '.csv' for file_name
    table_name = file_name[:-4]
    # Get the file object from aws s3
    obj = s3.get_object(Bucket=bucket, Key=file_name)
    # Read the data from file object
    data = pd.read_csv(obj['Body'])

    try:
        frame = data.to_sql(table_name, dbConnection, if_exists='fail', index=False, chunksize=10000)
    except Exception as e:
        print(e)

    print('loaded....', file_name)

dbConnection.close()