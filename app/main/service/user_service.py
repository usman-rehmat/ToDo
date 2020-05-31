from flask import render_template, url_for
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from app.main import db, get_mail
from app.main.model.User import User
from flask_mail import Message
from app.main import app
from app.main.model.User import User
import os

def create(data):
    try:
        new_user = User(
            email =data['email'],
            password=data['password']
        )
        
        # Email 
        #tooken
        token = generate_confirmation_token(new_user.email)
        #confirm url
        confirm_url = 'http://127.0.0.1:5000/user/confirmemail/' + token
        html = render_template("email.html", confirm_url=confirm_url)
        #subject
        subject = "Please confirm your email"
        # send email
        send_email(new_user.email, subject, html)

        # Email sent on
        new_user.email_confirmation_sent_on = datetime.utcnow()
        save_changes(new_user)
        response_object = {
                    'status': 'success',
                    'message': 'Sign Up successfully'
                }
        return response_object, 200
    except Exception as e:
        print(repr(e))
        response_object = {
            'status': 'fail',
            'message': 'Data is not correctly defined',
        }
        return response_object, 409
def send_email(to, subject, template):
    try:

        with get_mail().connect() as conn : 
            msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender= app.config['MAIL_USERNAME'])
            conn.send(msg)
        return True
    except Exception as e:
        print(repr(e))
        return False
    
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email
def confirmedEmail(user):
    user.email_confirmed = True
    user.authenticated = True
    user.email_confirmed_on = datetime.now()
    save_changes(user)

def login_user(data):
    try:
        # fetch the user data
        user = User.query.filter_by(email=data.get('email')).first()
        if user and user.check_password(data.get('password')):
            auth_token = User.encode_auth_token(user.id)
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'Authorization': auth_token.decode()
                }
                return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'email or password does not match.'
            }
            return response_object, 401

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Try again'
        }
        return response_object, 500
def get_logged_in_user(new_request):
    # get the auth token
    auth_token = new_request.headers.get('Authorization')
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        print(resp)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email
                }
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': resp
        }
        return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return response_object, 401

def save_changes(data):
    db.session.add(data)
    db.session.commit()

