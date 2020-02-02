from decouple import config

class Config:
    DEBUG = config('DEBUG')
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
