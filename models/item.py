import sqlite3
from db import db


# we removed the @classmethod cz we dont have to pass a item ..we just insert update or find itself ..ie the object for
# these methods to be called -  udated_item.update() -- so cls, item --> self

class ItemModel(db.Model):
    __tablename__ = 'items'

    # only these columns will be used i =n db operations ,,other columns are ignored
    # tell sqlalchemy how to read the columns from __table__
    # then read and pump them into __init__ and create a object fro each row
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # table_name.column_name
    # instead of joins use below - to find a store using store_id
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items where name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row)

        # above all code replaced by below and returns a ItemModel object ...
        # sice @classmethod replsce -- ItemModel.query() -- cls.query()
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):

        # insert and update by the same method so .. replace with insert() and update() methods
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()