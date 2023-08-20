#!/usr/bin/python3

""" Imports storage modules and packages """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
