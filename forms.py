from flask.ext.wtf import Form
from wtforms import TextField, SelectField, SubmitField

class addForm(Form):
	netid = TextField("Netid")
	company = TextField("Company")
	where = TextField("Location")
	when = SelectField("Semester", choices=[('Summer', 'Summer'), ('Spring', 'Spring'), ('Fall', 'Fall')])