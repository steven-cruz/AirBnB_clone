#!/usr/bin/python3
"""
Unittest for base_model
"""


import unittest
from models.base_model import BaseModel
import os
import pep8


class Test_BaseModel(unittest.TestCase):
    """
    Test class BaseModel
    """
    def test_docstring(self):
        """Checks if the docstring exists"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """
        Setups test
        """
        pass

    def tearDown(self):
        """
        Resets tests
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """Pass an arg into the instance"""
        b1 = BaseModel(12)
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertFalse(hasattr(b1, "12"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = BaseModel(name="Red")
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, "name"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))

    def test_str_method(self):
        """Tests to see if the method is printing accurately"""
        b1 = BaseModel()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[BaseModel] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """Tests the instance before using the todict conversion"""
        b1 = BaseModel()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "BaseModel")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """Tests instances after using to_dict conversion"""
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(test_dict['__class__'], "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Tests if the instance of BaseModel have been correctly made"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))

    def test_save(self):
        """Tests to see if the save fuction works"""
        b1 = BaseModel()
        b1.save()
        b_dict = b1.to_dict()
        self.assertNotEqual(b_dict['created_at'], b_dict['updated_at'])
