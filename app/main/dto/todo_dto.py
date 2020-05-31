from flask_restplus import Namespace, fields

class TodoDto:
    api = Namespace('todo', description='Todo related operations')
    todo = api.model('todo', {
        'title': fields.String(required=True, description='title of task'),
        'completion_status': fields.Boolean(required=False, description='completion status of task'),
        'description': fields.String(required=True, description='task description'),
        'due_date': fields.DateTime(required=True, description='due date of taks'),
        'completion_date': fields.DateTime(required=False, description='completeion date of task'),
        'user_id': fields.String(description='user who creates this task')
    })