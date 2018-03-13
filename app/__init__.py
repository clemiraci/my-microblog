from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # load configuration variables from Config class

from app import routes