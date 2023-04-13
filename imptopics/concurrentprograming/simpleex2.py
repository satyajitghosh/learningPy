import asyncio
import time

'''

'''

async def task1():
    print('Send first email.')
    await asyncio.sleep(6)
    print('First Email Reply')

async def task2():
    print('Send second email.')
    await asyncio.sleep(2)
    print('Second Email Reply')

async def task3():
    print('Send third email.')
    await asyncio.sleep(4)
    print('Third Email Reply')

async def runsync():
    '''
    This function runs the three tasks syncronously (sequentially).
    As a result, this takes around 12 seconds to complete.
    '''
    await task1()
    await task2()
    await task3()

async def runasync():

    '''
    This function runs the three tasks asyncronously (non-sequentially or concurrently).
    As a result, this takes around 6 seconds to complete.
    '''

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())

    await t1,t2,t3

async def runasyncwithgather():

    '''
    This function runs the three tasks asyncronously (non-sequentially or concurrently).
    As a result, this takes around 6 seconds to complete.
    Just uses a different syntax.
    '''
    await asyncio.gather(task1(),task2(),task3())

start = time.perf_counter()
asyncio.run(runsync())
end = time.perf_counter()
runtime = end - start
print(f'Time taken for Synchronous Vrsion = {runtime}')

start = time.perf_counter()
asyncio.run(runasync())
end = time.perf_counter()
runtime = end - start
print(f'Time taken for Asynchronous version = {runtime}')

start = time.perf_counter()
asyncio.run(runasyncwithgather())
end = time.perf_counter()
runtime = end - start
print(f'Time taken for Asynchronous version (with gather) = {runtime}')
