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
		for i in range(len(query)):
			if query[i] == '' or query[i] is 'None':
				query[i] = '%'
		markers = Marker.query.filter(Marker.company.like(query[0]), Marker.job_type.like(query[1]), Marker.rating >= query[2], Marker.valid == 1).all()
	return markers

if __name__ == '__main__':
	app.run()