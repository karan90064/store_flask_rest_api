import sqlite3
from db import db


# import db and extend to say that it is an entity and we are going to map it with databse
# and perform DB operations

# we transfered this class cz it not a resource - external repreentation
# it is a model - internal repreentation
class UserModel(db.Model):
    __tablename__ = 'users'

    # only these columns will be used i =n db operations ,,other columns are ignored
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_by_username(cls, username):
        # sqlalchemy maintains comm , cursor, build queries and also convert them to objects (with id anme price)
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
