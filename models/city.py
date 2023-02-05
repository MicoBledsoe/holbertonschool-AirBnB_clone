#!/usr/bin/python3
"""
Project 0x00. AirBnB clone - The console
    class definition of City
    inherits from the BaseModel class
    imported from models.base_model
    attributes are state_id, name
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        subclass City, inherits from BaseModel
            attributes:
                state_id, an empty string
                name, an empty string
    """
    state_id = ""
    name = ""
