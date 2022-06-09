import os


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'A SECRET KEY')

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

app_config = ProductionConfig()