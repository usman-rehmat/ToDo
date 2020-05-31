from flask import request
from flask_restplus import Resource

from app.main.service import todo_service   
from ..dto.todo_dto import TodoDto 
from app.main.util.decorator import token_required

api = TodoDto.api


@api.route('/create')
class CreateTask(Resource):
    """
        Create task Resource
    """
    @api.doc('Create Task')
    @token_required
    @api.expect(TodoDto.todo, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return todo_service.create(data=post_data)
