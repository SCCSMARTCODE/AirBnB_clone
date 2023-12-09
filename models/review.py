#!/usr/bin/python3
"""
This module contains the
        Review class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review, inheriting from BaseModel.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
