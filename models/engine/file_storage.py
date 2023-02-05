#!/usr/bin/python3
"""
    Project 0x00. AirBnB clone - The console
        class FileStorage, which serializes and deserializes
        instances into a JSON string
"""
from models.base_model import BaseModel
import json
import os
import models
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """
        class FileStorage which serializes and deserializes instances
            to and from a JSON file
        private attributes:
            __file_path
            __objects
        public instance methods:
            all, new, save, reload
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the objects within a dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        adds new object into __objects dictionary with key being
            `<obj class name>.id`
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        creates empty dictionary TempDict of keys the same as within __objects
            and value calls to_dict which convert __objects into dictionary,
            and opens specified file and stores JSON representation of TempDict
        """
        TempDict = {}
        for key, value in self.__objects.items():
            TempDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf=8') as f:
            f.write(json.dumps(TempDict))

    def reload(self):
        """
        desrializes a JSON file if one exists, if not does nothing
        otherwise, does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                LoadDict = json.loads(f.read())
            for key, val in LoadDict.items():
                self.__objects[key] = eval(val["__class__"])(**val)
