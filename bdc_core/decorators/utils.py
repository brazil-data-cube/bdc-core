#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Utility decorators for Brazil Data Cube Core app."""

import contextlib
import os

from bdc_core.utils.logger import logger


@contextlib.contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit.

    Exceptions:
        FileNotFoundError when could not change to directory provided.

    Args:
        path (str): Directory to change

    Returns:
        str Path to the changed directory

    Example:
        >>> import os
        >>> from tempfile import gettempdir
        >>> from bdc_core.decorators.utils import working_directory
        ...
        ...
        >>> TEMP_DIR = gettempdir()
        >>> @working_directory(TEMP_DIR)
        ... def create_file(filename):
        ...     # Create file in Temporary folder
        ...     print('Current dir: {}'.format(os.getcwd()))
        ...     with open(filename, 'w') as f:
        ...         f.write('Hello World')
    """
    owd = os.getcwd()
    logger.debug("Changing working dir from %s to %s", owd, path)
    try:
        os.chdir(path)
        yield path
    finally:
        logger.debug("Back to working dir %s", owd)
        os.chdir(owd)
