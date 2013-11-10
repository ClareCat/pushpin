from flask import render_template, request, redirect
import sys
import os
from models import Marker
from forms import addForm
from run import app, db

@app.route('/')
def index(query=None):
	form = addForm()
	markers = get_markers(query)
	return render_template('index.html', markers=markers, form=form)

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		form = addForm()
		newData = Marker(form.company.data.title(), form.where.data.title(), form.when.data.title(), -1.0, int(form.culture.data), int(form.work.data), int(form.overall.data))
		db.session.add(newData)
		db.session.commit()
	return redirect(url_for('index'))

def get_markers(query):
	markers = None
	if not query:
		markers = Marker.query.all()
	return markers
"""
	print lat_long
	sys.stdout.flush()
	test = Marker("test", "USA")
	db.session.add(test)
	db.session.commit()
	print test
	sys.stdout.flush()
"""



if __name__ == '__main__':
	app.run()