#!/usr/bin/python3
""" making review inherence from basemodel """


import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ Public Class attributes """
    place_id = ""
    user_id = ""
    text = ""
