#!/usr/bin/env python3
"""Defining a cache class"""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    """Representation of cache class"""

    def __init__(self):
        """Initialization of Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a random set of data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
