from flask import render_template
import sys
import os
from models import Marker
from run import app, db

@app.route('/')
def index(lat_long=(40, -100)):
	print lat_long
	sys.stdout.flush()
	test = Marker("test", "USA")
	db.session.add(test)
	db.session.commit()
	print test
	sys.stdout.flush()
	return render_template('index.html', lat_long=lat_long)