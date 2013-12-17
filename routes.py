from flask import flash, render_template, request, redirect, url_for
import sys
import os
from models import Marker
from forms import addForm, queryForm
from run import app, db

@app.route('/')
def index():
	markers = get_markers(None)
	if request.args.get('rating', '') != "":
		query = [request.args.get('company', ''), request.args.get('job_type', ''), int(request.args.get('rating', ''))]
		markers = get_markers(query)
	addform = addForm()
	queryform = queryForm()
	return render_template('index.html', markers=markers, addform=addform, queryform=queryform)

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = addForm(request.form)
	if request.method == 'POST' and form.validate():
		newData = Marker(form.netid.data.title(), form.company.data.title(), form.where.data.title(), form.job_type.data.title(), -1.0, int(form.rating.data))
		db.session.add(newData)
		db.session.commit()
		flash("Successful!")
	else:
		flash("I'm sorry, there was an error with your input")
	return redirect(url_for('index'))

@app.route('/query', methods=['GET', 'POST'])
def query():
	query = queryForm(request.form)
	return redirect(url_for('index', rating=query.rating.data, company=query.company.data, job_type=query.job_type.data))

def get_markers(query):
	if not query:
		markers = Marker.query.filter(Marker.valid == 1).all()
	else:
		q = []
		if query[0] != '':
			q.append(" AND company = '{}'".format(query[0]))
		if query[1] != 'None':
			q.append(" AND job_type = '{}'".format(query[1]))

		search = "SELECT * FROM marker WHERE rating >= {} AND valid = 1".format(query[2])
		for item in q:
			search += item
		search += ';'
		print search

		markers = Marker.query.from_statement(search)
	return markers

if __name__ == '__main__':
	app.run()