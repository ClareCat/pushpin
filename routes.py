from flask import render_template, request, redirect, url_for
import sys
import os
from models import Marker
from forms import addForm, queryForm
from run import app, db

@app.route('/')
def index():
	markers = get_markers(None)
	if request.args.get('semester', '') != "":
		query = [request.args.get('semester', ''), int(request.args.get('culture', '')), int(request.args.get('work', '')), int(request.args.get('overall', ''))]
		markers = get_markers(query)
	addform = addForm()
	queryform = queryForm()
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
	query = queryForm()
	return redirect(url_for('index', semester=query.when.data, culture=query.culture.data, work=query.work.data, overall=query.overall.data))

def get_markers(query):
	if not query:
		markers = Marker.query.all()
	else:
		if query[0] == 'None':
			query[0] = '%'
		markers = Marker.query.filter(Marker.semester.like(query[0]), Marker.culture >= query[1], Marker.work >= query[2], Marker.overall >= query[3]).all()
	return markers


@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'


if __name__ == '__main__':
	app.run()