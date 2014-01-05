from flask.ext.wtf import Form
from wtforms import TextField, SelectField, SelectMultipleField, RadioField, validators

class addForm(Form):
	netid = TextField("Netid", [validators.Required()])
	company = TextField("Company Name", [validators.Required()])
	where = TextField("Location", [validators.Required()])
	job_type = SelectField("Type", [validators.Required()], choices=[('Internship', 'Internship'), ('Co-op', 'Co-op'), ('Fulltime', 'Fulltime')])
	rating = SelectField("How would you rate your experience?", [validators.Required()], choices=[('1', 'It was ugly'), ('2', 'It was bad'), ('3', 'It was okay'), ('4', 'It was good'), ('5', 'It was awesome!')])
	major = SelectField("Your ")

class queryForm(Form):
	company = TextField("Company Name")
	job_type = SelectMultipleField("Type", choices=[('Internship', 'Internship'), ('Co-Op', 'Co-op'), ('Fulltime', 'Fulltime')])
	rating = SelectField("Rated at least", choices=[('0','Any Rating'), ('1', 'Ugly'), ('2', 'Bad'), ('3', 'Okay'), ('4', 'Good'), ('5', 'Awesome')])
