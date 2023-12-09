#!/usr/bin/python3
"""This module contains the User class that inherits from BaseModel"""

from .base_models import BaseModel


class User(BaseModel):
    """A class representing a user, inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
