#!/usr/bin/python3
"""Class FileStorage"""


import json
import models
from models.base_model import BaseModel
from datetime import datetime



class FileStorage:
    """Private class attributes for Class FileStorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary with objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Returns __objects with obj set as key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file inside"""
        save_file = self.__file_path
        new_dict = {}
        for key, item in self.__objects.items():
            new_dict[key] = item.to_dict()
        with open(save_file, "w", encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists; otherwise, do nothing
        """
        reload_dict = {}
        try:
            with open(FileStorage.__file_path, mode="r") as a_file:
                reload_dict = (json.load(a_file))
                for key, value in reload_dict.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
