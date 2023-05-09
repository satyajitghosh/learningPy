import asyncio

async def main(myname):
    print('Hello')
    await asyncio.sleep(0.5)
    print(myname)

async def runner():

    task1 = asyncio.create_task(main('Satyajit'))
    task2 = asyncio.create_task(main('Ghosh'))
    await task1,task2
    print('Done')

async def runnerwithgather():

    task1 = asyncio.create_task(main('Satyajit'))
    task2 = asyncio.create_task(main('Ghosh'))
    await asyncio.gather(task1,task2)
    print('Done')

async def runnerwithgatherwithloop():

    tasks = []
    names = ['Ram','Shyam','Jodu','Modu']
    for name in names:
        tasks.append(asyncio.create_task(main(name)))
    await asyncio.gather(*tasks)
    print('Done')

asyncio.run(runnerwithgatherwithloop())