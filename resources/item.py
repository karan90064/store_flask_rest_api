from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

from models.item import ItemModel


class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be empty."
                        )
    parser.add_argument('store_id',
                        type=float,
                        required=True,
                        help="Every item needs a store id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'item doesnot exist'}, 404

    def post(self, name):

        # error first approach
        # if next(filter(lambda x: x['name'] == name, items), None):  --  replace this with
        # use get() - @classmethod - using self or Item.find_by_name(name)
        if ItemModel.find_by_name(name):
            return {"message": 'item with name {} already exists'.format(name)}, 400

        request_data = Items.parser.parse_args()

        # item = ItemModel(name, request_data['price'], request_data['store_id'])
        item = ItemModel(name, **request_data)

        # items.append(item) -- replace this with
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "insert into items values (?, ?)"
        # cursor.execute(query, (item['name'], item['price']))
        # connection.commit()
        # connection.close()

        # replace the above with the class method
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
            # Internal server error- server fault not users

        return {'added item': item.json()}, 201

    def delete(self, name):

        # 1 - filter
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))  -- use sqllite

        # 2 - conn and cursor
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "delete from items where name=?"
        # cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()

        # 3 - sqlalchemy
        item = ItemModel.find_by_name(name)

        if item:
            item.delete()

        return {'message': 'item --{}-- deleted'.format(name)}, 200

    def put(self, name):
        data = Items.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemsList(Resource):
    def get(self):

        # we have to convert the query result to list first

        # list comprehension
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

        # other way could be - good if you code with other lang developers
        # map lambda func to all result objects
        # convert to list
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

