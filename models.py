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
		lat = int(float(data['lat']))
		lon = int(float(data['lon']))
		return lat, lon


class Marker(db.Model):
	__tablename__ = "marker"
	id = db.Column(db.Integer, primary_key=True)
	company = db.Column(db.String(80))
	location = db.Column(db.String(120))
	lat = db.Column(db.Integer(4))
	lon = db.Column(db.Integer(4))
	
	def __init__(self, company, location):
		self.company = company
		self.location = location
		self.lat, self.lon = get_lat_long(location)

		
