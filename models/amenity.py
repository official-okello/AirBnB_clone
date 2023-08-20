#!/usr/bin/python3

"""Defines booking amenities"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from"""
    name = ""
