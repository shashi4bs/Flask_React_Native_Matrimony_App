import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# secret key for forms
    SECRET_KEY = "PASSWORD"
	#mysql database URL
    #SQLALCHEMY_DATABASE_URI = "mysql://shashi:shashi@localhost/matrimony"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
