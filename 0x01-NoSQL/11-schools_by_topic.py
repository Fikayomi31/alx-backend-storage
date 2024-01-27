#!/usr/bin/env python3
"""function that return the list of school specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of specfic topic"""
    schools =  mongo_collection.find()
    return [school for school in schools if topic in school.get('topics', [])]
