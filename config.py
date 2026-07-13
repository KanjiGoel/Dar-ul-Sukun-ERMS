import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dar_ul_sukun_secret_key')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False