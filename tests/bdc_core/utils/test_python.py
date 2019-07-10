import unittest

from bdc_core.utils.python import replace_by_list

class TestPython(unittest.TestCase):
    
    def test_replace_by_list(self):
        list_sub = [":", ",", "."]
        string = "test name_list.py, ok!"
        new_string = replace_by_list(string, list_sub, "_")
        self.assertEqual("test name_list_py_ ok!", new_string)
        