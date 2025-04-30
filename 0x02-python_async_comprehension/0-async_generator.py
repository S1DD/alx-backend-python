#!/usr/bin/env python3
"""
Generates 10 random values every second
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
