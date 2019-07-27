# initial configurations , App and database instance is initialised here

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

App = Flask(__name__) #.....................App instance 
App.config.from_object(Config) #............set configuraions to App
db = SQLAlchemy(App) #......................initialise connection to database with flask_sqlalchemy
migrate = Migrate(App, db) #................track database for commits modifiiactions can downgraded and upgraded easily with Flask_Migrate
login = LoginManager(App) #.................Manages Login and Session.
bootstrap = Bootstrap(App)
from app import routes,models,errors
