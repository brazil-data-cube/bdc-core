"""
This file contains the commom validators used through
Brazil Data Cube projects
"""

from functools import wraps
from flask import request
from jsonschema import draft7_format_checker, \
                       SchemaError, \
                       validate, \
                       ValidationError
from werkzeug.exceptions import BadRequest
from bdc_core.utils.logger import logger


def require_model(schema, draft=draft7_format_checker):
    """
    Utility to require JSON schema object to validate request
    query arguments (request.args).
    You can use it with APIResource in order to format BadRequestError output.

    TODO: Improve decorator to support request POST data values

    Args:
        schema (dict): JSON schema with Python Dictionaries.
        draft (jsonschema.FormatChecker, optional): JSON Schema format.

    Raises:
        BadRequest: When request arguments do not match with JSON schema.

    Example:
        Here an example usage with Flask application:

        >>> from bdc_core.decorators.validators import require_model
        >>> from flask import request, Flask
        >>> app = Flask(__name__)
        >>> coverage_schema = {
        >>>     "type": "object",
        >>>     "properties": {"coverage": {"type": "string"}},
        >>>     "required": ["coverage"]
        >>> }
        >>> @app.route('/')
        >>> @require_model(coverage_schema)
        >>> def get_coverage():
        >>>     '''Now its safe to get coverage name'''
        >>>     coverage_name = request.args['coverage']
        >>>     return 'Coverage "{}" provided'.format(coverage_name)
        >>> if __name__ == '__main__':
        >>>     app.run()
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_function(*args, **kwargs):
            try:
                validate(instance=request.args,
                         schema=schema,
                         format_checker=draft)
            except (SchemaError, ValidationError) as e:
                logger.debug('Validate JSONSchema %s', e.message)
                raise BadRequest(e.message)
            return fn(*args, **kwargs)
        return decorated_function
    return decorator
