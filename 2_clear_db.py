#!/usr/bin/python3
"""
Script to clear all objects from every table in the database using DBStorage.
"""

from models import storage

# Import all model classes
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def clear_all_objects():
    """Clears all objects from every table in the database."""
    storage.reload()

    # Iterate through each model class and delete all records
    for cls in [Amenity, City, Place, Review, State, User]:
        # Query all records of the current model class
        all_objects = storage.all(cls)
        for obj in all_objects.values():
            storage.delete(obj)
        storage.save()

if __name__ == "__main__":
    clear_all_objects()
