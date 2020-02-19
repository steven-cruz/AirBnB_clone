#!/usr/bin/python3
""" making state inherence from basemodel """


import models
from models.base_model import BaseModel


class State(BaseModel):
    """ public Class attributes """
    name = ""
