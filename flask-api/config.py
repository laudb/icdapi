import os
from dotenv import load_dotenv

load_dotenv()

# base path
base_dir = os.path.abspath(os.path.dirname(__file__))

# variables
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")
test_db_name = os.getenv("test_db_name")

# Database URLs
db_url = f"postgresql//{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
test_db_url = f"postgresql//{db_user}:{db_password}@{db_host}:{db_port}/{test_db_name}"

# Environment Variables
class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = db_url


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = test_db_url
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False