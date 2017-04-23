from database import db


# Create data storage
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    birth_date = db.Column(db.Date)
    password = db.Column(db.String)


class Computer(db.Model):
    __tablename__ = 'computer'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', backref=db.backref('computers'))
