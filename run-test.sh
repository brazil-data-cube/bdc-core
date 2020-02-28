
#!/usr/bin/env bash
#
# This file is part of BDC Core.
# Copyright (C) 2019 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle bdc_core && \
isort --check-only --diff --recursive bdc_core/*.py && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
pytest &&
sphinx-build -qnW --color -b doctest doc/sphinx/ doc/sphinx/_build/doctest