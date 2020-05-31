from datetime import datetime
from app.main import db
from app.main.model.Todo import Todo


def create(data):
    try:
        new_task = Todo()

        new_task.title  = data['title']
        new_task.completion_status = data['completion_status']
        new_task.due_date=data['due_date']
        new_task.created_on=datetime.utcnow()
        new_task.user_id = data['user_id']
        if data.get('completion_date') is not None:
            new_task.completion_date=data['completion_date']
    
        save_changes(new_task)
        response_object = {
            'status': 'success',
            'message': 'Task created sucessfully',
        }
        return response_object, 200
    except Exception  as ex:
        print(str(ex))
        response_object = {
            'status': 'fail',
            'message': 'Data is not correctly defined',
        }
        return response_object, 409

def update(data):
    try:
        task = Todo.query.filter_by(id=data.get('id')).first()
        print(task)
        if task:
            if data.get('title') is not None:
                task.title=data['title']
            if data.get('completion_status') is not None:
                task.completion_status = data['completion_status']
            if data.get('completion_date') is not None:
                task.completion_date=data['completion_date']
            if data.get('due_date') is not None:
                task.due_date=data['due_date']

            save_changes(task)
            response_object = {
                'status': 'sucess',
                'message': 'Task updated successfully',
            }
            return response_object, 200
        else:
            response_object = {
            'status': 'fail',
            'message': 'Task not found',
            }
            return response_object, 400
    except Exception  as ex:
        print(str(ex))
        response_object = {
            'status': 'fail',
            'message': 'Data is not correctly defined',
        }
        return response_object, 409
def getUserTasks(id, page = 0, page_size =10):
    page = int(page)
    page_size = int(page_size)
    try:
        task_list = Todo.query.filter_by(user_id=id).order_by(Todo.created_on.desc()).paginate(page, page_size, False)
        print(task_list.items)
        return task_list.items, 200
    except Exception  as ex:
        print(str(ex))
        response_object = {
            'status': 'fail',
            'message': 'Not able to delete this task',
        }
        return response_object, 409
def delete(id):
    try:
        print(id)
        task = Todo.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        response_object = {
            'status': 'sucess',
            'message': 'Task deleted successfully',
        }
        return response_object, 200
    except Exception  as ex:
        print(str(ex))
        response_object = {
            'status': 'fail',
            'message': 'Not able to delete this task',
        }
        return response_object, 409

def get_all_tasks():
    return Todo.query.all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()

