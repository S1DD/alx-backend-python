#!/usr/bin/env python3
"""
Returns a random value after a certain amound of seconds have elapsed
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random number of seconds
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
