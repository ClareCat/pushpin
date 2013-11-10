from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
app = Flask(__name__)
app.debug = True
heroku = Heroku(app)
db = SQLAlchemy(app)
db.init_app(app)


if __name__ == '__main__':
	app.run()
