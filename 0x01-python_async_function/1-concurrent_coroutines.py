#!/usr/bin/env python3

"""Contains a method that spawns wait_random n times with a
specified delay between each call."""

from typings import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified delay
    between each call.
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
     waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
