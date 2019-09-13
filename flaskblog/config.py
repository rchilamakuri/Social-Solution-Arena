import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')



os.environ['SECRET_KEY']='f5bd67a9bd1a94c02f1c5fd952623676'
os.environ['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
os.environ['MAIL_USERNAME']='Raghuram.chilamakuri2@gmail.com'
os.environ['MAIL_PASSWORD']='Madhuri@009'