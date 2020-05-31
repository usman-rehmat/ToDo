from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail



from .config import config_by_name
from flask_email_verifier import EmailVerifier
import os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'main/template')
print(TEMPLATE_PATH)
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
app = Flask(__name__, template_folder = TEMPLATE_PATH)
   


def create_app(config_name):
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    return app

def get_email_verifier():
    return EmailVerifier(app)
def get_mail():
    return Mail(app)
