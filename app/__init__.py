from flask_restplus import Api
from flask import Blueprint

from .main.controller.todo_controller import api as todo_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='ToDo tasks',
          version='1.0',
          description='User manages to do tasks'
          )

api.add_namespace(todo_ns, path='/todo')
api.add_namespace(user_ns, path='/user')