#!/usr/bin/python3
"""
Unittest for amenity
"""


from models.amenity import Amenity
import pep8
import os
import unittest


class Test_Amenity(unittest.TestCase):
    """
    Unittest for the class Amenity
    """

    def test_docstring(self):
        """Checks for docstring"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_init_arg(self):
        """pass in arg to new instance"""
        b1 = Amenity(23)
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = Amenity(name="AC")
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_hasattribute(self):
        """Tests if the instance of BaseModel has been correctly made"""
        b1 = Amenity()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
