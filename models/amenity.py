#!/usr/bin/python3
"""This module contains the
        Amenity class that inherits from BaseModel"""

# Importing the BaseModel class from the base_models module
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an Amenity.

    Attributes:
        name (str): The name of the Amenity.
    """
    name = ""
