#!/usr/bin/env python3
"""a python module to measure the execution time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_time() -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    asyncio.gather(*tasks)
    end_time = time.perf_counter
    return (end_time - start_time)
