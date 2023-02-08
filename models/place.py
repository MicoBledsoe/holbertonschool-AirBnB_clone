#!/usr/bin/python3
"""
Project 0x00. AirBnB clone - The console
    class definition of Place
    inherits from the BaseModel class
    imported from models.base_model
    attributes city_id, user_id, state_id, name, description,
    number_of_rooms, number_of_bathrooms, max guests, price_by_night,
    latitude, longitude, amenity_ids
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    subclass place, inherits from BaseModel
            attributes:
                state_id, empty string
                name, empty string
                description, empty string
                number of rooms, int 0
                number of bathrooms, int 0
                max guests, int 0
                price by night, int 0
                latitude, float 0.0
                longitude, float 0.0
                amenity ids, empty list
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
