#!/usr/bin/env python3
"""Change all topics of a document"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a document
    """
    key = {"name": name}
    values = {"$set": {"topics": topics}}
    mongo_collection.update_many(key, values)
