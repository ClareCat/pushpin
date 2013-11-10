from flask import render_template
import sys
import os
from models import Marker
from run import app, db

@app.route('/')
def index():
	#all_markers = Marker.query.all()
	all_markers = []
	all_markers.append(Marker("test1", "Urbana"))
	all_markers.append(Marker("test2", "San Diego"))
	all_markers.append(Marker("test3", "Seattle"))
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