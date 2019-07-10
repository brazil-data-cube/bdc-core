from bdc_core.decorators.validators import require_model
from flask import Flask, request
from werkzeug.exceptions import BadRequest
import json
import unittest


app = Flask('')
app.config['TESTING'] = True


schema = {
    "type": "object",
    "properties": {"coverage": {"type": "string"}},
    "required": ["coverage"]
}

@app.route("/")
@require_model(schema)
def route_index():
    return json.dumps(request.args)


class TestRequireModel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_invalid_schema(self):
        resp = self.app.get('/')

        self.assertEqual(400, resp.status_code)
        self.assertIn("'coverage' is a required property", resp.data.decode('utf-8'))

    def test_valid_schema(self):
        resp = self.app.get('/?coverage=coverageExample')

        self.assertEqual(200, resp.status_code)
        self.assertIn(json.dumps({"coverage": "coverageExample"}), resp.data.decode('utf-8'))
