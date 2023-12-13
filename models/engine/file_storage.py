#!/usr/bin/python3
"""
This module contains the file or database structuring class.
"""

import json
import os


class FileStorage:
    """
    A class for file or database structuring.
    """
        __file_path = "file.json"
        __object = {}

    def all(self):
        """
        Return all the stored objects.

        Returns:
            dict: A dictionary containing all the stored objects.
        """
        return self.__object

    def new(self, obj):
        """
        Add a new object to the stored objects.

        Args:
            obj (object): The object to be added.
        """
        self.__object.update({
            obj.__class__.__name__ + '.' + obj.id: obj.to_dict()
        })

    def save(self):
        """
        Save the stored objects to a file.
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__object, f)

    def reload(self):
        """
        Reload the stored objects from a file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__object = json.load(f)
