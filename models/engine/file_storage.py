""" Class commentary """


import json


class FileStorage():
    """ This class handels Json files with instances, it has 2 private class
        attributes and 4 public instance methods"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self):
        """ Initializes the class. """
        self.__file_path = "file.json"
        self.__objects = {}

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""
    def all(self):
        """ Returns a dictionary containing __objects. """
        return self.__objects

    def new(self, obj):
        """ Creates a new dictionary representation to save into a file. """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Saves the data into the HDD via a file. """
        with open(self.__file_path, 'a') as jfile:
            json.dump(self.__objects, jfile)

    def reload(self):
        """ Loads the data from the HDD into an instance. """
        try:
            with open(self.__file_path, 'r') as jfile:
                json_load = json.loads(jfile.read())
                for key, val in json_load.items():
                    new_key = eval(val['__class__'])(**val)
                    self.__objects = new_key

        except:
            pass

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """-- Class --"""
    """-----------"""

    """-----------"""
    """-- Static -"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
