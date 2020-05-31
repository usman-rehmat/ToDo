import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['EMAIL_VERIFIER_KEY'] = 'at_PEwsnUYOFdJAnygO4fCCsEJNSExQP'

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key') # os.environ.get('SECRET_KEY')
    EMAIL_VERIFIER_KEY = os.getenv('EMAIL_VERIFIER_KEY', 'at_PEwsnUYOFdJAnygO4fCCsEJNSExQP')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/todo' # os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = 'my_precious_token' # os.environ.get('SECURITY_PASSWORD_SALT')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = '*************' # os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = '************' #os.environ.get('MAIL_PASSWORD')
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
email_verifier_key = Config.EMAIL_VERIFIER_KEY
