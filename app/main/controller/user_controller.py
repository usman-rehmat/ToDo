from flask import request, make_response
from flask_restplus import Resource

from app.main.service import user_service   
from ..dto.user_dto import UserDto 
from app.main import get_email_verifier 
from datetime import datetime
from app.main.model.User import User

api = UserDto.api

@api.route('/signup')
class CreateUser(Resource):
    """
        Signup Resource
    """
    @api.doc('Sign Up')
    @api.expect(UserDto.user, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return user_service.create(data=post_data)


@api.route('/email/<email>', endpoint='email')
@api.param('email', 'The User email')
@api.response(404, 'User not found.')
class EmailVerification(Resource):
    """
    Email verification
    """
    @api.doc('Email verification')
    def post(self, email):
        # Retrieve an info for the given email address
        email_address_info = get_email_verifier().verify(email)
        if email_address_info is not None:
            # data = dumps(loads(email_address_info.json_string), indent=4)
            resp = make_response(email_address_info.json_string, 200)
            resp.headers['Content-Type'] = 'application/json'
        else:
            resp = make_response('None', 404)
        return resp
@api.route('/confirmemail/<token>')
@api.param('token', 'Token')
@api.response(404, 'Token not found.')
class ConfirmEmail(Resource):
    """
    Email confirmation
    """
    @api.doc('Confirmation email')
    def get(self,token):
        
        try:
            email = user_service.confirm_token(token)
        except:
            return False
        
        user = User.query.filter_by(email=email).first_or_404()
        if user.email_confirmed:
            return "user already confirmed"
        else:
            user_service.confirmedEmail(user)
        return True
@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(UserDto.user, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        print(post_data)
        return user_service.login_user(data=post_data)

@api.route('/task_reminder')
class TaskReminder(Resource):
    """
        Task Reminder
    """
    @api.doc('Task reminder')
    def get(self):
        # get the post data
        return user_service.sendReminderEmail()
