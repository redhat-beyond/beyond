from datetime import datetime
from baboon import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"id: {self.id}\nusername: {self.username}\n creation date:{self.creation_date}"

    def serialize(self):
        return {

            'id': self.id,
            'username': self.username,
            'creation_date': self.creation_date
        }
