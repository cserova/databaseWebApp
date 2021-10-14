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
3. Activate virtual env
    ```
   . venv/bin/activate
    ```
4. Run the application
   ```
   flask run
   ```
5. Deactivate virtual env
    ```
   deactivate
   ```
6. AWS Hosting commands
   ```
   ssh ec2-user@ec2-18-191-148-86.us-east-2.compute.amazonaws.com
   tmux new -s databaseWebApp
   tmux ls
   tmux attach -t databaseWebApp
   tmux kill-session -t databaseWebApp
   ```