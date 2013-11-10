from flask import render_template
import sys
import os
from models import Marker
from run import app, db

@app.route('/')
def index():
	all_markers = Marker.query.all()
	return render_template('index.html', markers=all_markers)

if __name__ == '__main__':
	app.run()
"""
	print lat_long
	sys.stdout.flush()
	test = Marker("test", "USA")
	db.session.add(test)
	db.session.commit()
	print test
	sys.stdout.flush()
"""