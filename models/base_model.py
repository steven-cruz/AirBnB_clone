#!/usr/bin/python3
""" Class commentary """


import uuid
import json
from datetime import datetime


class BaseModel():
    """ This class is the base model for all the AirBnB subclasses. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, *args, **kwargs):
        """ Initializes the class. """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    formt = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], formt)
                elif key != '__class__':
                    self.__dict__[key] = kwargs[key]

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""

    def __str__(self):
        """ Defines what the class should print. """
        name = self.__class__.__name__
        text = ("[{}] ({}) {}".format(name, self.id, self.__dict__))
        return text

    def save(self):
        """ Updates the public instance attribute "update_at" with the current
            datetime.                                                       """
        up = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
            instance.                                                       """
        a_dict = {}
        a_dict['__class__'] = self.__class__.__name__

        if self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, datetime) is True:
                    value = value.isoformat()
                a_dict[key] = value

        return a_dict
