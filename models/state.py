#!/usr/bin/python3
"""
This module contains the
        State class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    A class representing a state, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
