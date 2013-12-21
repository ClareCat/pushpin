from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
app = Flask(__name__)
app.secret_key = 'a'
app.debug = True
heroku = Heroku(app)
if not app.config['SQLALCHEMY_DATABASE_URI']:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/pushpin'
db = SQLAlchemy(app)
db.init_app(app)
