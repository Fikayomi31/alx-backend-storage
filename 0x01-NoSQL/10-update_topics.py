#!/usr/bin/env python3
"""Change all topics of a document"""


def update_topics(mongo_collection, name, topics):
    """doc"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
