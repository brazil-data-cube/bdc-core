import jwt
import os
from flask import request
from functools import wraps
from werkzeug.exceptions import Forbidden, HTTPException, Unauthorized

def get_token():
    try:
        bearer, authorization = request.headers['Authorization'].split()
        if 'bearer' not in bearer.lower():
            raise Forbidden('Invalid token. Please login!')
        return authorization

    except Exception:
        raise Forbidden('Token is required. Please login!')

def validate_scope(scope_required, scope_token):
    if scope_required:
        service, function, actions = scope_required.split(':')
        if (service != scope_token['type'] and scope_token['type'] != '*') or \
            (function not in scope_token['name'] or scope_token['name'] != '*') or \
            (actions not in scope_token['actions'] or scope_token['actions'] != '*'):
            raise Unauthorized('Scope not allowed!')

def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not os.environ.get('CLIENT_SECRET_KEY'):
            raise HTTPException('Set CLIENT_SECRET_KEY in environment variable')

        try:
            token = get_token()
            payload = jwt.decode(token, os.environ.get('CLIENT_SECRET_KEY'))
            if payload.get('user_id') and payload.get('access_token'):
                request.user_id = payload['user_id']
                validate_scope(kwargs['scope'], payload['access'][0])
                return func(*args, **kwargs)
            else:
                raise Forbidden('Incomplete token. Please login!')           

        except jwt.ExpiredSignatureError:
            raise Forbidden('This token has expired. Please login!')
        except jwt.InvalidTokenError:
            raise Forbidden('Invalid token. Please login!')
    return wrapper