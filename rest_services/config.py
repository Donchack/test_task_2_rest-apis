import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')
    SERVER_NAME = os.environ.get('SERVER_IP_PORT', '127.0.0.1:5000')

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

app_config = DevelopmentConfig()