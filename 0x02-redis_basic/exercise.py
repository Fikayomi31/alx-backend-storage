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
        """Storing a random set of data
        Arg:
            data: can be either str, bytes, int, float
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[
                Callable] = None) -> Union[str, bytes, int, float]:
        """Converting data back to it desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get a string"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get a int"""
        return self.get(key, int)
