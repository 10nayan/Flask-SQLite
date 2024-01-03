from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#ID, name, age, nationality ID, and birthdate.
class Person(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer())
    country = db.relationship('Country', backref = 'country', uselist = False)
    nationality_id = db.Column(db.Integer(), db.ForeignKey('country.id'), unique = True, nullable = False)
    date_of_birth = db.Column(db.Date())
    birthplace_id = db.Column(db.String(20))

class Country(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    country_name = db.Column(db.String(20), nullable = False, unique = True)
    capital = db.Column(db.String(20), nullable = False)

class Place(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(20), nullable = False, unique = True)
    state = db.Column(db.String(20), nullable = False)
    country = db.relationship('Country', backref = 'country', uselist = False)
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id'), unique = True, nullable = False)
