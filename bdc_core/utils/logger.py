"""
Base logger handler for Brazil Data Cube projects.

By default, the `logger` already set to provided module. In this way, you can
handle your log application based in module context.

You can also set logger to log to file and customize file format.
https://docs.python.org/3/howto/logging.html

Example:
    >>> from bdc_core.utils.logger import logger
    >>>
    >>>
    >>> def executeSQL(sql):
    >>>     logger.debug('Preparing SQL to execute %s', sql)
    >>>     # Do operations
    >>>     logger.info('Query executed successfully')
    >>>
    >>> executeSQL('SELECT now()')
"""

import logging
import os


def create_logger(application=None):
    """
    Creates a logger object context for application

    You can customize a logger for your module and handle individual scopes

    Args:
        application (string) - Application name.
            It usually represents `__name__`. Default is `root` channel
    """
    if not application:
        application = 'root'

    internal_logger = logging.getLogger(application)

    if os.environ.get('ENVIRONMENT') == 'DevelopmentConfig':
        logging.basicConfig(level=logging.DEBUG)
        internal_logger.setLevel(logging.DEBUG)

    return internal_logger


logger = create_logger(__name__)
