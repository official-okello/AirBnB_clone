#!/usr/bin/python3

"""Defines a city"""


from models.base_model import BaseModel


class City(BaseModel):
    """Defines city to check from"""
    state_id = ""
    name = ""
