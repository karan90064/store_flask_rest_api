from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security_sqllite import authenticate, identity
from resources.users import UserRegister
from resources.item import Items, ItemsList
from resources.store import Store, StoreList

app = Flask(__name__)

# import some sqlalchemy configs
# tracks if object is changed but not commited to db ..it uses resources so turn it off - the flask sqlalchemy
# instead SQLALCHEMY has its own tracker so we off only flask's one not the sqlalchemy ones
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'secretkeyrandom'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

# Note
# it only creates tables which it sees
# import  from resources.store import Store  --> from models.store import StoreModel --> make the table


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')


# app.run(port=5000, debug=True)
# when we import any file then it loads the file - check all the classes - checks all the methods
# and also RUN the statements like print() etc..
# so if we import app.py then it would run -- app.run(port=5000, debug=True) -- not expected/wrong
#
# whenever we run - python app.py -- pythons gives a special __name__ to the file -- __main__
# so we use below method .. only if this is the file ran (not imported)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)