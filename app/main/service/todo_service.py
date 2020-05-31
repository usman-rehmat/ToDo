from datetime import datetime
from app.main import db
from app.main.model.Todo import Todo


def create(data):
    try:
        new_task = Todo(
            title=data['title'],
            completion_status = data['completion_status'],
            completion_date=data['completion_date'],
            due_date=data['due_date'],
            created_on=datetime.utcnow(),
            user_id = data['user_id']
        )
        save_changes(new_task)
        return True
    except Exception  as ex:
        print(str(ex))
        response_object = {
            'status': 'fail',
            'message': 'Data is not correctly defined',
        }
        return response_object, 409


def get_all_tasks():
    return Todo.query.all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()

