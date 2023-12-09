#!/usr/bin/python3
"""
This is my init
        module getting me my storage file
"""

# Importing the file_storage module from the engine package
from models.engine import file_storage

# Creating an instance of the FileStorage class from the file_storage module
storage = file_storage.FileStorage()

# Reloading the storage, which likely loads data from a file into memory
storage.reload()
