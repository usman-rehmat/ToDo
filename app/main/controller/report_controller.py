from flask import request, make_response
from flask_restplus import Resource

from app.main.service import report_service   
from ..dto.report_dto import ReportDto 
from app.main import get_email_verifier 
from datetime import datetime
from app.main.model.User import User

api = ReportDto.api


@api.route('/taskstatus')
class TaskStatus(Resource):
    """
        Task status Resource
    """
    @api.doc('Task status')
    def get(self):
        # get the post data
        return report_service.get_task_status()
