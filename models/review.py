#!/usr/bin/python3
"""This module contains the Review class that inherits from BaseModel"""

from .base_models import BaseModel


class Review(BaseModel):
    """A class representing a review, inheriting from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
