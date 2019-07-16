import json
import os
import sys
import unittest
from flask import Flask
from flask_restplus import Api
from werkzeug.exceptions import NotFound
from bdc_core.utils.flask import APIResource


flask_app = Flask('')
flask_app.config['TESTING'] = True
api = Api(flask_app)
ns = api.namespace('test')


class TestAPIResource(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.test_client()

    def test_response_json(self):
        expected_response = {"status": True}

        # pylint: disable=unused-variable
        @ns.route('/')
        class TestResource(APIResource):
            def get(self):
                return expected_response

        resp = self.app.get('/test/')

        self.assertEqual(200, resp.status_code)
        self.assertEqual('application/json', resp.content_type)
        self.assertEqual(json.loads(resp.data.decode('utf-8')), expected_response)

    def test_handle_http_exceptions(self):
        # pylint: disable=unused-variable
        @ns.route('/notfound')
        class TestResource(APIResource):
            def get(self):
                raise NotFound("Resource not found")

        resp = self.app.get('/test/notfound')

        self.assertEqual(404, resp.status_code)
        self.assertEqual('application/json', resp.content_type)

        body = json.loads(resp.data.decode('utf-8'))

        self.assertEqual(body['message'], 'Resource not found')
        self.assertEqual(body['code'], 404)

    def test_base_exceptions_as_server_error(self):
        # pylint: disable=unused-variable
        @ns.route('/python-error')
        class TestResource(APIResource):
            def get(self):
                raise IOError("IOError")

        resp = self.app.get('/test/python-error')

        self.assertEqual(500, resp.status_code)
        self.assertEqual('application/json', resp.content_type)

        body = json.loads(resp.data.decode('utf-8'))

        self.assertEqual(body['message'], 'IOError')
        self.assertEqual(body['code'], 500)