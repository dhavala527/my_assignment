from app import db
from sqlalchemy.dialects.postgresql import JSON



class Result(db.Model):
    __tablename__ = 'geographics'

    name = db.Column(db.String(128))
    lat = db.Column(db.Float)	#	Latitude value
    lng = db.Column(db.Float)	#	Longitude value

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng
        
def insert_statement(name, lat, lng):
	obj = Result(name, lat, lng)
    session.add(obj)
    session.commit()
