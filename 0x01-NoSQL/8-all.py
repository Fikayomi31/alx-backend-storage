#!/usr/bin/env python3
"""List all document"""


def list_all(mongo_collection):
    """return the list"""
    return mongo_collection.find()
