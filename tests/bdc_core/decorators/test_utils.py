import os
from tempfile import gettempdir
from unittest import TestCase
from bdc_core.decorators import utils


class TestDecoratorsUtils(TestCase):
    @staticmethod
    def get_working_dir(directory):
        @utils.working_directory(directory)
        def working_dir_wrapper():
            return os.getcwd()

        return working_dir_wrapper

    def test_change_working_dir_to_temp(self):
        test_dir = os.path.abspath(os.getcwd())
        expected_dir = gettempdir()

        get_working_dir = TestDecoratorsUtils.get_working_dir(expected_dir)

        temp_dir = get_working_dir()

        self.assertNotEqual(test_dir, temp_dir)
        self.assertEqual(temp_dir, expected_dir)

    def test_throw_error_invalid_directory(self):
        get_working_dir = TestDecoratorsUtils.get_working_dir('/fake/It-Does-Not-Exists')

        with self.assertRaises(FileNotFoundError):
            get_working_dir()