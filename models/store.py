from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # says we have a relationship with ItemModel ...
    # so waht reln -  so it goes to 'ItemModel' --  and finds store_id id there as a foreign key to <id> here
    # many to one so -  items will be a list

    # whenever we make an store object - sqlalc will make objects for all items having that sqtore_id
    # many items -  slower store object creation -
    # so donot go into items and create items object - lazy='dynamic'

    # but .json method will give error --  cz we are not making items object
    # item in self.items --->>  item in self.items.all() -->
    # lazy='dynamic' items no longer a list of items - becomes a query builder
    # so whenever we do store_obj.json() --> run a query self.items.all() so will become slow
    # creating store fast - calling json() slow

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()