from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_caching import Cache
from .config import config_by_name
from flask_email_verifier import EmailVerifier
import logging
import os


APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'main/template')
print(TEMPLATE_PATH)
db = SQLAlchemy()
flask_bcrypt = Bcrypt()

cache = Cache(config={'CACHE_TYPE': 'simple'})
app = Flask(__name__, template_folder = TEMPLATE_PATH)
cache.init_app(app)
logging.basicConfig(level=logging.DEBUG)


def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    return app

def get_email_verifier():
    return EmailVerifier(app)
def get_mail():
    return Mail(app)
def getCache():
    return cache.init_app(app)