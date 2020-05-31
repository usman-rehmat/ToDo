from functools import wraps
from flask import request
from app.main.service import user_service 
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = user_service.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated
