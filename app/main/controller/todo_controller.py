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

@api.route('/update')
class UpdateTask(Resource):
    """
        Update task Resource
    """
    @api.doc('Update Task')
    @token_required
    @api.expect(TodoDto.todoUpdate, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return todo_service.update(data=post_data)


@api.route('/delete/<id>')
@api.param('id', 'The Task id')
class DeleteTask(Resource):
    """
        Delete task Resource
    """
    @api.doc('Delete Task')
    @token_required
   
    def post(self, id):
        # get the post data
        return todo_service.delete(id)

@api.route('/getUserTasks/<id>/<page>/<page_size>')
@api.param('id', 'The User id')
@api.param('page', 'page number')
@api.param('page_size', 'page size')
class GerUserTask(Resource):
    """
        Delete task Resource
    """
    @api.doc('Delete Task')
    @token_required
    @api.marshal_list_with(TodoDto.todo, envelope='data')
    def get(self, id, page=0, page_size=10):
        # get the post data
        return todo_service.getUserTasks(id, page, page_size)

