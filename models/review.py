#!/usr/bin/python3
"""Project 0x00. AirBnB clone - The console
    class definition of Review
    inherits from the BaseModel class
    imported from models.base_model
    attributes are place_id, uder_id, and text
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        subclass Review, inherits from BaseModel
            attributes:
                place_id, an empty string
                user_id, an empty string
                text, an empty string
    """
    place_id = ""
    user_id = ""
    text = ""
