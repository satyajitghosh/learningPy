import asyncio
import time

'''
The three tasks are executed concurrently.
As evident from output, when the sleep times for t1,t2,t3 are 6,2,4 respectively,
the order of starting is t1,t2,t3, but the order of finishing is t2,t3,t1.
The three tasks are started almost at the same time, and run concurrntly.
The one with the longest wait time finishes last.

The total time taken is 6 seconds - which is almost same as the largest wait time
amongst the three functions. t1 is the largest at 6 sec.

Without concurrency this would have taken - 6+2+4 = 12 sec.
'''

async def task1():
    print('Send first email.')
    asyncio.create_task(task2())
    await asyncio.sleep(6)
    print('First Email Reply')

async def task2():
    print('Send second email.')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('Second Email Reply')

async def task3():
    print('Send third email.')
    await asyncio.sleep(4)
    print('Third Email Reply')

start = time.perf_counter()
asyncio.run(task1())
end = time.perf_counter()
runtime = end - start
print(f'Time taken = {runtime}')
