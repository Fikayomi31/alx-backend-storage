#!/usr/bin/env python3
"""function that return the list of school specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of specfic topic"""
    return mongo_collection.find({"topic": topic})
