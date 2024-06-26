#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = FileStorage.__objects
        if cls is None:
            return objs
        if type(cls) is str:
            cls = eval(cls)
        cls_objs = {key: obj for key, obj in objs.items() if type(obj) is cls}
        return cls_objs

    def new(self, obj):
        """Adds new object to storage dictionary"""
        type(self).__objects.update({obj.to_dict()['__class__'] + '.' +
                                     obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an obj from __objects"""
        if obj is not None:
            key = obj.to_dict()['__class__'] + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                FileStorage.save(self)

    def close(self):
        """ Calls the reload() method to deserialize the JSON file to
        objects. """
        self.reload()
