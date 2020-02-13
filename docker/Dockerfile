#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

FROM brazildatacube/base:0.1

ADD . /bdc-core

WORKDIR /bdc-core

RUN pip3 install pip --upgrade && \
    pip install wheel && \
    pip install -e .[all]
