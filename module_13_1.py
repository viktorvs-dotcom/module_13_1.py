import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep((i * 5) / power)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Apollon', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Pasha', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
