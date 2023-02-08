#!/usr/bin/python3
"""
    Project 0x00. AirBnB clone - The console
        class definition of User
        inherits from the BaseModel class
        imported from models.base_model
        attributes are email, password, first_name, last_name
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        subclass User, inherits from BaseModel
                attributes:
                    email, empty string
                    password, empty string
                    first_name, empty string
                    last_name, empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
