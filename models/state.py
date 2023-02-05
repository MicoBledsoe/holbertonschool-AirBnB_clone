#!/usr/bin/python3
"""Project 0x00. AirBnB clone - The console
    class definition of State
    inherits from the BaseModel class
    imported from models.base_model
"""

from models.base_model import BaseModel


class State(BaseModel):
    """subclass State
            attributes:
            name, an empty string
    """
    name = ""
