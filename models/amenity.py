#!/usr/bin/python3
""" making amenity inherence from basemodel """


import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Public Class attributes """
    name = ""
