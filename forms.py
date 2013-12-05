from flask.ext.wtf import Form
from wtforms import TextField, SelectField, SubmitField, DecimalField

class addForm(Form):
	company = TextField("Company")
	where = TextField("Location")
	when = SelectField("Semester", choices=[('Summer', 'Summer'), ('Spring', 'Spring'), ('Fall', 'Fall')])
	salary = DecimalField("Salary(per month)", places=2)
	culture = SelectField("Company Culture", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	work = SelectField("Work", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	overall = SelectField("Overall Experience", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

class queryForm(Form):
	when = SelectField("Semester", choices=[('None','None'), ('Summer', 'Summer'), ('Spring', 'Spring'), ('Fall', 'Fall')])
	culture = SelectField("Company Culture at least", choices=[('0',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	work = SelectField("Work at least", choices=[('0',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	overall = SelectField("Overall Experience at least", choices=[('0',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
