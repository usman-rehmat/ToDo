from flask_restplus import Api
from flask import Blueprint

from .main.controller.todo_controller import api as todo_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.report_controller import api as report_ns
from apscheduler.schedulers.background import BackgroundScheduler
from app.main.service import user_service

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='ToDo tasks',
          version='1.0',
          description='User manages to do tasks'
          )

api.add_namespace(todo_ns, path='/todo')
api.add_namespace(user_ns, path='/user')
api.add_namespace(report_ns, path='/report')

def sendReminderEmail():
    """ Send reminder email """
    print(" Daily scheduler is alive!")
    user_service.sendReminderEmail()
    
sched = BackgroundScheduler(daemon=True)
sched.add_job(sendReminderEmail,'cron',day_of_week='mon-fri', hour=0, minute=0, second=0)
sched.start()


