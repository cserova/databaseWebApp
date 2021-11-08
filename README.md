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
3. Install tmux
    ```
   sudo yum install tmux
    ```
4. Activate virtual env
    ```
   . venv/bin/activate
    ```
5. Run the application
   ```
   flask run
   ```
6. Deactivate virtual env
    ```
   deactivate
   ```
7. AWS Hosting commands
   ```
   ssh ec2-user@ec2-18-191-38-21.us-east-2.compute.amazonaws.com
   tmux new -s databaseWebApp
   tmux ls
   tmux attach -t databaseWebApp
   tmux kill-session -t databaseWebApp
   source venv/bin/activate
   flask run --host=0.0.0.0 --port=8080

   ```