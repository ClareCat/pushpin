from run import app, db
import urllib2
import urllib
import json
		

def get_lat_long(location):
		url = 'http://nominatim.openstreetmap.org/search?'
		params = urllib.urlencode(dict(q=location, format='json'))
		response = urllib.urlopen(url+params)
		response = response.read()
		data = json.loads(response)[0]
		lat = float(data['lat'])
		lon = float(data['lon'])
		return lat, lon


class Marker(db.Model):
	__tablename__ = "marker"
	id = db.Column(db.Integer, primary_key=True)
	company = db.Column(db.String(80))
	location = db.Column(db.String(120))
	lat = db.Column(db.Numeric(16))
	lon = db.Column(db.Numeric(16))
	semester = db.Column(db.String(20))
	salary = db.Column(db.Numeric(16))
	culture = db.Column(db.Integer(2))
	work = db.Column(db.Integer(2))
	overall = db.Column(db.Integer(2))


	
	def __init__(self, company, location, semester, salary, culture, work, overall):
		self.company = company
		self.location = location
		self.lat, self.lon = get_lat_long(location)
		self.semester = semester
		self.salary = salary
		self.culture = culture
		self.work = work
		self.overall = overall