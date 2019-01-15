import os

class Config(object):
	# secret key for forms
    SECRET_KEY = "PASSWORD"
	#mysql database URL
    SQLALCHEMY_DATABASE_URI = "mysql://shashi:shashi@localhost/matrimony"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
