from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#ID, name, age, nationality ID, and birthdate.
class Person(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer())
    nationality_id = db.Column(db.String(100))
    birthplace = db.Column(db.String(100))
