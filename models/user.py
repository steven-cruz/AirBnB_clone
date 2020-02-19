#!/usr/bin/python3
""" making user inherence from basemodel """


Basemodel = __import__.(base_model).BaseModel


class User(BaseModel):
""" the new class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
