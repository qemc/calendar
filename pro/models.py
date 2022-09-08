from pro import login_manager
from pro import db
from flask_login import UserMixin
from pro import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=60),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=100), nullable=False)
    events = db.relationship('Event', backref=' creator', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, atempted_password):
        return bcrypt.check_password_hash(self.password_hash, atempted_password)


class Event(db.Model):
    event_id = db.Column(db.Integer(), primary_key=True)
    event_name = db.Column(db.String(length=200), nullable=False)
    event_date = db.Column(db.Date(), nullable=False)
    event_time = db.Column(db.Time(), nullable=False)
    event_creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
    

