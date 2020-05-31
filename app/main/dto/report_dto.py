from flask_restplus import Namespace, fields

class ReportDto:
    api = Namespace('report', description='Todo related operations')
    report = api.model('report', {
       
    })