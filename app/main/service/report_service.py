from flask import render_template, url_for
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from app.main import db, get_mail
from app.main.model.User import User
from flask_mail import Message
from app.main import app
from app.main.model.Todo import Todo
import os
from app.main import cache

@cache.cached(timeout=(15*60*60))
def get_task_status():
    try:
            
        totalTasks =  db.session.query(Todo).count()
        print("total_tasks : " , totalTasks)
        completedTasks = db.session.query(Todo).filter_by(completion_status=True).count()
        pendingTasks = db.session.query(Todo).filter_by(completion_status=False).count()
        response_object = {
                'status': 'sucess',
                'data': {
                    'total_tasks' : totalTasks,
                    'completed_tasks' : completedTasks,
                    'pending_tasks' : pendingTasks 
                }
            }
        return response_object, 200
    except Exception as e:
        print(str(e))
        response_object = {
                'status': 'failure',
                
            }
        return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()