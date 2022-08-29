
from pro import db




#Klasa, w sumie bardzo podobna rzecz do klasy w cpp, zdecydowanie łatwiej z niej korzystać
#niż bez niej xD

class User(db.Model):

    id = db.Column(db.Integer(), primary_key = True)
    user_name = db.Column(db.String(length=30), nullable = False, unique = True)
    email_address = db.Column(db.String(length=60), nullable = False, unique = True)
    password_hash = db.Column(db.String(length=100), nullable = False)
    #events = db.relationship('Event', backref='creator', lazy=True)


class Event(db.Model):
    event_id = db.Column(db.Integer(), primary_key = True)
    event_name = db.Column(db.String(length=200), nullable = False, unique = False)
    event_date = db.Column(db.Date(), nullable = False)
    event_time = db.Column(db.DateTime(), nullable = False)
    #event_creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'    



