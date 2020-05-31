from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='The user email address'),
        'password': fields.String(required=True, description='The user password ')
    })