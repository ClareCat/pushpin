from flask import render_template, request, redirect, url_for
import sys
import os
from models import Marker
from forms import addForm, queryForm
from run import app, db

@app.route('/')
def index(query=None):
	addform = addForm()
	queryform = queryForm()
	markers = get_markers(query)
	return render_template('index.html', markers=markers, addform=addform, queryform=queryform)

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		form = addForm()
		newData = Marker(form.company.data.title(), form.where.data.title(), form.when.data.title(), -1.0, int(form.culture.data), int(form.work.data), int(form.overall.data))
		db.session.add(newData)
		db.session.commit()
	return redirect(url_for('index'))

@app.route('/query', methods=['GET', 'POST'])
def query():
	query = None
	if request.method == 'POST':
		form = queryForm()
		s = Marker.query.filter(company=="test")
		print s
		sys.stdout.flush()
	return redirect(url_for('index', query=s))

def get_markers(query):
	markers = query
	if not query:
		markers = Marker.query.all()
	return markers


if __name__ == '__main__':
	app.run()