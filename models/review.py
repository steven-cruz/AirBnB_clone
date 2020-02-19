#!/usr/bin/python3
""" making review inherence from basemodel """


from models.base_model import BaseModel

class Review(Basemodel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs)
        super().__init__(self, *args, **kwargs)
