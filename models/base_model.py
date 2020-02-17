#!/usr/bin/python3
import uuid
import json
from datetime import datetime

""" Class commentary """
class BaseModel:
    """ Class description. """
    """====================================================================="""
    """=================== INIT & CLASS VARIABLES =========================="""
    """====================================================================="""
    def __init__(self,  *args, **kwargs):
        """ Initializes the class """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
    """====================================================================="""
    """============================ METHODS ================================"""
    """====================================================================="""
    def __str__(self):
        name = name = self.__class__.__name__
        st = ("[{}] ({}) {}".format(name, self.id, self.__dict__))
        return st
    def save(self):
        up = datetime.now()
        updated_at = datetime.isoformat(up)
        return updated_at
    def to_dict(self):
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = datetime.isoformat(self.created_at)
        dic['updated_at'] = datetime.isoformat(self.updated_at)
        return dic
    """----------"""
    """- Public -"""
    """----------"""
    """-----------"""
    """- Private -"""
    """-----------"""
    """-----------"""
    """- Class ---"""
    """-----------"""
    """-----------"""
    """- Static --"""
    """-----------"""
    """====================================================================="""
    """==================== SETTERS & GETTERS =============================="""
    """=====================================================================""" 
