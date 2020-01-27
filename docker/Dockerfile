FROM brazildatacube/base:0.1

ADD . /bdc-core

WORKDIR /bdc-core

RUN pip3 install pip --upgrade && \
    pip install wheel && \
    pip install -e .[tests,docs]
