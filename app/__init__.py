from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login LoginManager


app = Flask(__name__)
app.config.from_object(Config) # load configuration variables from Config class
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' # name of the login view function

# models defines struture of the database
from app import routes, models