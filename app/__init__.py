from flask import Flask
from config import Config
#from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
#db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from app import routes