#!/usr/bin/python3
"""This module contains the City class that inherits from BaseModel"""

from .base_models import BaseModel
from uuid import uuid4


class City(BaseModel):
    """A class representing a city, inheriting from BaseModel"""

    state_id = ""
    name = ""
