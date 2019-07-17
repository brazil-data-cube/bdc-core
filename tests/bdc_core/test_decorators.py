import json
import unittest
from flask import Flask, request
from werkzeug.exceptions import BadRequest
from bdc_core.decorators.validators import require_model


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

    def test_missing_required_property(self):
        resp = self.app.get('/')

        self.assertEqual(400, resp.status_code)
        self.assertIn("'coverage' is a required property", resp.data.decode('utf-8'))

    def test_exception_on_invalid_schema(self):
        invalid_schema = {
            "type": "object",
            "properties": {"coverage": {"type": "any"}},
            "required": ["coverage"]
        }

        # pylint: disable=unused-variable
        @app.route('/invalid')
        @require_model(invalid_schema)
        def route_invalid():
            return "Should not reach here"

        resp = self.app.get('/invalid')
        self.assertEqual(400, resp.status_code)
        self.assertIn("\'any\' is not valid under any of the given schemas", resp.data.decode('utf-8'))

    def test_valid_schema(self):
        resp = self.app.get('/?coverage=coverageExample')

        self.assertEqual(200, resp.status_code)
        self.assertIn(json.dumps({"coverage": "coverageExample"}), resp.data.decode('utf-8'))