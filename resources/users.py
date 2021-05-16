import sqlite3
from flask_restful import Resource, request, reqparse

from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be empty')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be empty')

    def post(self):
        # data = request.get_json()
        data = UserRegister.parser.parse_args()

        if UserModel.get_user_by_username(data['username']):
            return {'message': 'user {} already exists'.format(data['username'])}, 400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()

        # NOTE - good
        # user = UserModel(data['username'], data['password'])
        # NOTE -  unpacking - data is a dict so ** - key:value, key:value, key:value, key:value --so on
        # we also have parser so wwe know nothig more than username password will go to __init__ of UserModel

        user = UserModel( **data)
        user.save_to_db()

        return {'message': 'user {} added successfully'.format(data['username'])}, 201
