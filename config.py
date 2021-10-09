import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATBASE_URL')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False