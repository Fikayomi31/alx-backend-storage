#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b'first')
print(cache.get(cache.store.__qualname__))
