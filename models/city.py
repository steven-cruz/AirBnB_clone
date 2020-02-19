#!/usr/bin/python3
""" making city inherence from basemodel """


import models
from models.base_model import BaseModel


class City(BaseModel):
    """ pulic class attributes """
    state_id = ""
    name = ""
