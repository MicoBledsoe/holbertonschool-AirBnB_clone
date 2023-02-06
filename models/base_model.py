#!/usr/bin/python3
"""The BaseModel class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ TWO ARGS IMPLEMENT"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            s = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(self.created_at, s)
            self.updated_at = datetime.strptime(self.updated_at, s)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)


    def __str__(self):
        """returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """DICTIONARY"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
