from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'store {} already exists'.format(name)}, 400


        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store."}, 500

        return {'store added': store.json()}, 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete()

        return {'store deelted': store.name}


class StoreList(Resource):
    def get(self):
        # return {'stores': [store.json() for store in StoreModel.query.all()]}
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}