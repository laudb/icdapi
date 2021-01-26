import os
from dotenv import load_dotenv
load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
db_user = os.getenv('db_user')
db_password =  os.getenv('db_password')
db_host =  os.getenv('db_host')
db_name = os.getenv('db_name')

db_url= f'postgresql//{db_user}:{db_password}@{db_host}:5433/{db_name}'

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_DATABASE_URI = db_url

class DevConfig(BaseConfig):
    DEBUG=True

class TestConfig(BaseConfig):
    DEBUG=True

class ProdConfig(BaseConfig):
    DEBUG=False