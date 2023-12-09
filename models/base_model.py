#!/usr/bin/python3
"""This is the class that contains the base-model"""

# Importing the required modules
import uuid
import datetime
from .__init__ import storage


class BaseModel:
    """A base model class that defines
        common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance"""
        # Generating a unique ID using the uuid module
        self.id = str(uuid.uuid4())

        # Setting the created_at and updated_at attributes to the current date
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # Checking if any keyword arguments are provided
        if len(kwargs) >= 1:
            # Iterating over the keyword arguments
            for x in kwargs.keys():
                # Checking if the argument is created_at or updated_at
                if x == "created_at" or x == "updated_at":
                    # Converting the provided datetime string to a datetime
                    self.__dict__[x] = datetime.datetime.fromisoformat(
                            kwargs[x]
                    )
                else:
                    # Assigning the provided value to the corresponding
                    self.__dict__[x] = kwargs[x]
        else:
            # If no keyword arguments are provided, adding the instance
            storage.new(self)

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Save the instance"""
        # Updating the updated_at attribute to the current datetime
        self.updated_at = datetime.datetime.now()

        # Adding the instance to the storage and saving the changes
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object"""
        # Creating a dictionary representation of the object
        dicti = self.__dict__.copy()
        dicti["updated_at"] = self.updated_at.isoformat()
        dicti["created_at"] = self.created_at.isoformat()
        dicti["__class__"] = self.__class__.__name__

        return dicti
