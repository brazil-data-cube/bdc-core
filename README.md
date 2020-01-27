# bdc-core
 Common basic functions among Brazil Data Cube applications


## Installing

Close `bdc-core` package with command:

```bash
git clone https://github.com/brazil-data-cube/bdc-core.git
cd bdc-core
```

You can install `bdc-core` package with setup.py:

```bash
python setup.py install
```

## Tests

In order to run tests, use the following command:

```bash
python -m pytest -v tests/
```

## Docker

Build docker image with following command:

```bash
docker build --tag brazildatacube/bdc-core:0.2 -f docker/Dockerfile .
```

After that, you can run tests with:

```bash
python -m pytest -v tests/
```