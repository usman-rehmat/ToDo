from datetime import datetime
from app.main import db
from app.main.model.Todo import Todo


def create(data):
    try:
        new_task = Todo(
            title=data['title'],
            completion_status=data['completion_status'],
            completion_date=data['completion_date'],
            due_date=data['due_date'],
            created_on=datetime.utcnow()
        )
        save_changes(new_task)
        return True
    except:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_tasks():
    return Todo.query.all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()

