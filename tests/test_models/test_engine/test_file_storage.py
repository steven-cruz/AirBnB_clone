#!/usr/bin/python3
"""File Storage Unit Tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import os
import sys
import pep8
import unittest


class Test_FileStorage(unittest.TestCase):
    """
    Test cases for class FileStorage
    """
    def test_docstring(self):
        """Checks if docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """Sets up the testing environment to not change the
        previous file storage
        """
        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'test_storage')

    def tearDown(self):
        """Removes the JSON file after test cases run """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', self.file_path)

    def test_instantiation(self):
        """Tests for proper instantiation"""
        temp_storage = FileStorage()
        self.assertIsInstance(temp_storage, FileStorage)

    def test_saves_new_instance(self):
        """Tests if file is being created """
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_all(self):
        """Tests the all method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        self.assertIsNotNone(temp_dict)
        self.assertEqual(type(temp_dict), dict)

    def test_new(self):
        """Tests the new method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        Holberton = User()
        Holberton.id = 972
        Holberton.name = "Holberton"
        temp_storage.new(Holberton)
        class_name = Holberton.__class__.__name__
        key = "{}.{}".format(class_name, str(Holberton.id))
        self.assertIsNotNone(temp_dict[key])

    def test_reload(self):
        """Tests for the reload method"""
        temp_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(temp_storage.reload(), None)
