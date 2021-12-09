# CS527 - Team 6 Project

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
   ssh-add MongoDB_Database.pem
   ssh -i MongoDB_Database.pem ec2-user@ec2-18-117-103-187.us-east-2.compute.amazonaws.com -v
   tmux new -s databaseWebApp
   tmux ls
   tmux attach -t databaseWebApp
   tmux kill-session -t databaseWebApp
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