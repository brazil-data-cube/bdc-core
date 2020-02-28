..
    This file is part of Python Module for BDC Core.
    Copyright (C) 2019 INPE.

    BDC Core is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

``bdc-core`` has few dependencies. Please, read the instructions below in order to install ``bdc-core``.


Production installation
-----------------------

Install from `GitHub <https://github.com/brazil-data-cube/bdc-core>`_:

.. code-block:: shell

        $ pip3 install git+https://github.com/brazil-data-cube/bdc-core@b-0.2


If you want to build the documentation and tests, please, install all the extras as follow:

.. code-block:: shell

        $ pip3 install git+https://github.com/brazil-data-cube/bdc-core@b-0.2#egg=bdc_core[all]


Development installation
------------------------

Clone the software repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/bdc-core.git


Go to the source code folder:

.. code-block:: shell

        $ cd bdc-core


Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]


Generate the documentation:

.. code-block:: shell

        $ python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/
