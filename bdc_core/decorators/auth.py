#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""
Authentication decorators such scope validator and token require
"""

from functools import wraps
import os
import jwt
from flask import request
from werkzeug.exceptions import Forbidden, HTTPException, Unauthorized


def get_token() -> str:
    """Retrieves token from request intercept"""

    try:
        bearer, authorization = request.headers['Authorization'].split()
        if 'bearer' not in bearer.lower():
            raise Forbidden('Invalid token. Please login!')
        return authorization

    except Exception:
        raise Forbidden('Token is required. Please login!')


def validate_scope(scope_required, scope_token):
    """
    Validates user token scope

    Args:
        scope_required (str) - OAuth scope required
        scope_token (dict) - Token object

    Exceptions:
        Unauthorized when scope is not allowed
    """

    if scope_required:
        service, function, actions = scope_required.split(':')

        if (service != scope_token['type'] and scope_token['type'] != '*') or \
            (function != scope_token['name'] and scope_token['name'] != '*') or \
            (actions not in scope_token['actions'] and '*' not in scope_token['actions']):
            raise Unauthorized('Scope not allowed!')


def require_oauth_scopes(scope):
    """
    Flask decorator to require OAuth scope in request intercept.

    Make sure to export the following variables:

        - `CLIENT_SECRET_KEY` OAuth client secret
        - `CLIENT_AUDIENCE` OAuth client audience control

    Example:
        >>> from flask import current_app
        >>> from bdc_core.decorators.auth import require_oauth_scopes
        >>>
        >>>
        >>> @current_app.route('/edit/<int:thing_id>')
        >>> @require_oauth_scopes('app:thing:edit')
        >>> def edit_something(thing_id):
        >>>     # put logic here
        >>>     return dict()

    Args:
        scope (str) - Required scope to match

    Returns:
        Wrapped function which performs request validation
    """

    def jwt_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not os.environ.get('CLIENT_SECRET_KEY'):
                raise HTTPException('Set CLIENT_SECRET_KEY in environment variable')
            if not os.environ.get('CLIENT_AUDIENCE'):
                raise HTTPException('Set CLIENT_AUDIENCE in environment variable')

            try:
                token = get_token()
                payload = jwt.decode(
                    token,
                    os.environ.get('CLIENT_SECRET_KEY'),
                    verify=True,
                    algorithms=['HS512'],
                    audience=os.environ.get('CLIENT_AUDIENCE')
                )

                if payload.get('user_id'):
                    request.user_id = payload['user_id']
                    validate_scope(scope, payload['access'][0])
                    return func(*args, **kwargs)

                raise Forbidden('Incomplete token. Please login!')

            except jwt.ExpiredSignatureError:
                raise Forbidden('This token has expired. Please login!')
            except jwt.InvalidTokenError:
                raise Forbidden('Invalid token. Please login!')
        return wrapper
    return jwt_required
