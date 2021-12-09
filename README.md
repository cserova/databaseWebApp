# CS527 - Team 6 Project

## Libraries
1. MySQL - pymysql
2. Redshift - psycopg2
3. MongoDb - pyodbc (with Simba MongoDB ODBC Driver 64-bit)

## App Features
1. Enabled Multi-line queries
2. Handled whitespace character (like spaces)
3. We have a keyboard shortcut too! xD ( ctrl + ‘ to run the query )
4. Display error messages
5. Prevent accidental “clears”
6. Download output as CSV or JSON
7. Copy table data to clipboard

## Usage
1. Install postgresql on mac
    ```
   brew install postgresql
   ```
2. Install Flask and required packages
    ```
   pip3 install -r requirements.txt
    ```
3. Install required libraries for mongoDb ODBC driver
   ```
   sudo yum install unixODBC-devel
   sudo yum install gcc
   sudo yum install gcc-c++
   sudo yum install python3-devel
   ```
4. Install tmux
    ```
   sudo yum install tmux
    ```
5. Activate virtual env
    ```
   . venv/bin/activate
    ```
6. Run the application
   ```
   flask run
   ```
7. Deactivate virtual env
    ```
   deactivate
   ```
8. AWS Hosting commands
   ```
   ssh -i MongoDB_Database.pem ec2-user@ec2-18-117-103-187.us-east-2.compute.amazonaws.com -v
   tmux new -s databaseWebApp
   tmux ls
   tmux attach -t databaseWebApp
   tmux kill-session -t databaseWebApp
   cd databaseWebApp
   source venv/bin/activate
   flask run --host=0.0.0.0 --port=8080
   ```
9. MongoDb commands
   ```
   mongoimport -d instacart_normal -c instacart_fact_table --type csv --file instacart_fact_table.csv --headerline
   mongoimport -d adniDB -c adnimerge_table --type csv --file modified_adnimerge.csv --headerline
   sudo systemctl start mongod
   sudo systemctl status mongod
   sudo systemctl enable mongod
   sudo systemctl stop mongod
   sudo systemctl restart mongod
   mongo
   ```