#!/usr/bin/python3
"""This module contains the Amenity class that inherits from BaseModel"""

# Importing the BaseModel class from the base_models module
from .base_models import BaseModel


# Defining the Amenity class that inherits from BaseModel
class Amenity(BaseModel):
    name = ""
