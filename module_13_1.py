import asyncio

async def start_strongman(name,power):
    print(f'силач {name} начал соревнование')
    for i in range (1,6):
        await asyncio.sleep(power)
        print(f'силач {name} поднял шар №{i}')
    print(f'силач {name} закончил соревнование')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Иванов',5))
    task2 = asyncio.create_task(start_strongman('Петров',4))
    task3 = asyncio.create_task(start_strongman('Сидоров',3))
    await task1,task2,task3
    print("соревнование закончено")

asyncio.run(start_tournament())

