#!/usr/bin/python3
""" making user inherence from basemodel """



from models.base_model import BaseModel


class User(BaseModel):


    email = ""
    password = ""
    first_name = ""
    last_name = ""
