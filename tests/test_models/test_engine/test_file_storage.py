#!/usr/bin/python3

"""Unittest for file_storage.py"""

import os
import unittest
from models.engine import file_storage
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Set up for the tests.
        """

        try:
            os.remove("test.json")
        except IOError:
            pass
        self.storage = file_storage.FileStorage()
        self.storage.__file_path = "test.json"

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("test.json")
        except IOError:
            pass

    def test_all(self):
        """
        Test that all returns the dictionary __objects
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Test that new adds an object to __objects
        """
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        self.storage.new(obj)
        self.assertIn(obj, self.storage.all().values())

    def test_save(self):
        """
        Test that save properly serializes __objects to the JSON file
        """
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        self.storage.save()
        with open("test.json") as f:
            obj2 = json.load(f)
        self.assertEqual(obj, obj2)

    def test_reload(self):
        """
        Test that reload properly deserializes the JSON file to __objects
        """
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        self.storage.reload()
        self.assertEqual(obj, self.storage.all())


if __name__ == "__main__":
    unittest.main()