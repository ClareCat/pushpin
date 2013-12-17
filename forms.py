from flask.ext.wtf import Form
from wtforms import TextField, SelectField, RadioField, validators

class addForm(Form):
	netid = TextField("Netid", [validators.Required()])
	company = TextField("Company", [validators.Required()])
	where = TextField("Location", [validators.Required()])
	job_type = RadioField("Type", [validators.Required()], choices=[('Internship', 'Internship'), ('Co-op', 'Co-op'), ('Fulltime', 'Fulltime')])
	rating = SelectField("How would you rate your experience?", [validators.Required()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

class queryForm(Form):
	company = TextField("Company")
	job_type = RadioField("Type", choices=[('Internship', 'Internship'), ('Co-op', 'Co-op'), ('Fulltime', 'Fulltime')])
	rating = SelectField("Rated at least", choices=[('0',''), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
