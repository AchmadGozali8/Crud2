import os

DEBUG = True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:ichal@localhost/crud'
SQLALCHEMY_TRACK_MODIFICATIONS = True
