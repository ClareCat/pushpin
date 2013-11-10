from flask import Flask, render_template
import sys

app = Flask(__name__)
app.debug = True

@app.route('/')
def index(lat_long=(40, -100)):
	print lat_long
	sys.stdout.flush()
	return render_template('index.html', lat_long=lat_long)


if __name__ == '__main__':
	app.run()
