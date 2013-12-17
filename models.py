from run import app, db
import urllib2
import urllib
import json, random
		
def get_lat_long(location):
	lat, lon = -1, -1
	try:
		url = 'http://nominatim.openstreetmap.org/search?'
		params = urllib.urlencode(dict(q=location, format='json'))
		response = urllib.urlopen(url+params)
		response = response.read()
		data = json.loads(response)[0]
		lat = float(data['lat']) + random.random()/100
		lon = float(data['lon']) - random.random()/100
	except ValueError:
		pass
	return lat, lon

class Marker(db.Model):
	__tablename__ = "marker"
	id = db.Column(db.Integer, primary_key=True)
	netid = db.Column(db.String(10))
	company = db.Column(db.String(80))
	location = db.Column(db.String(120))
	lat = db.Column(db.Numeric(16))
	lon = db.Column(db.Numeric(16))
	job_type = db.Column(db.String(20))
	salary = db.Column(db.Numeric(16))
	rating = db.Column(db.Integer(2))
	valid = db.Column(db.Integer(2))
	
	def __init__(self, netid, company, location, job_type, salary, rating):
		self.netid = netid
		self.company = company
		self.location = location
		self.lat, self.lon = get_lat_long(location)
		self.job_type = job_type
		self.salary = salary
		self.rating = rating
		self.valid = 1