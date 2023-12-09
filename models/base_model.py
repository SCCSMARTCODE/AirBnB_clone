#!/usr/bin/python3
"""
    This is the class that contains the base-model
"""

import uuid
import datetime
from . __init__ import storage


class BaseModel:
    """
    A base model class that defines common
                attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Notes:
            If keyword arguments are provided, the instance
                    attributes are set based on the provided values.
            Otherwise, the instance is added to the storage.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) >= 1:
            for x in kwargs.keys():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.datetime.fromisoformat(
                            kwargs[x]
                        )
                else:
                    self.__dict__[x] = kwargs[x]
        else:
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        space1 = self.__class__.__name__
        return "[{}] ({}) {}".format(space1, self.id, self.__dict__)

    def save(self):
        """
        Save the instance.

        Notes:
            This method updates the 'updated_at'
                        attribute to the current datetime,
            adds the instance to the storage, and saves the changes.
        """
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the object.

        Returns:
            dict: A dictionary representation of the object.
        """
        dicti = self.__dict__.copy()
        dicti["updated_at"] = self.updated_at.isoformat()
        dicti["created_at"] = self.created_at.isoformat()
        dicti["__class__"] = self.__class__.__name__

        return dicti
