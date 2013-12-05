from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
app = Flask(__name__)
app.secret_key = 'a'
app.debug = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/pushpin'
heroku = Heroku(app)
db = SQLAlchemy(app)
db.init_app(app)
