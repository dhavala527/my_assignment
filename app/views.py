from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/post_location')
def post_location():
	insert_statement('some_name', 45.12, 71.12)
	
	
	
@app.route('/get_using_postgres')
def get_using_postgres():
	


@app.route('/get_using_self')
def get_using_self():
	#	hardcoded values
	dist_per_lat = 111.00
	dist_per_lng = 111.321
	radius = 5
	lng_range = (dist_per_lng-5, dist_per_lng+5)
	lat_range = (dist_per_lat-5, dist_per_lat+5)
	return (lat_range, lng_range)


if __name__ == '__main__':
    app.run()
