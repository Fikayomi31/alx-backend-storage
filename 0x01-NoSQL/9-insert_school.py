#!/usr/bin/env python3
"""insert document in python"""


def insert_school(mongo_collection, **kwargs):
    """insert new document"""
    return mongo_collection.insert_one(kwargs).inserted_id
