#!/usr/bin/env python3
"""
Module for Redis cache.
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storing and managing data in Redis."""

    def __init__(self) -> None:
        """
        Stores instance of the Redis client as a private variable named _redis
        and flushes the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
