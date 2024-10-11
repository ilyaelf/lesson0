import queue
import random
import time
from threading import Thread


class Table():
    def __init__(self, n):
        self.number = n
        self.guest = None

    def __str__(self):
        return f'Стол №{self.number}'


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.place = None

    def __str__(self):
        return self.name

    def run(self):
        time.sleep(random.randint(3, 10))
        print(f'{self.name} закончил(-а) кушать и ушел(-ла)')
        print(f'{self.place} свободен')


class Cafe():
    def __init__(self, *table_list):
        self.table_list = table_list
        self.queue = queue.Queue()

    def guest_arrival(self, guests):
        try:
            for i in range(len(self.table_list)):
                self.table_list[i].guest = guests[i]
                print(f'{guests[i]} сел(-а) за {self.table_list[i]}')
                guests[i].table = self.table_list[i]
                guests[i].place = f'{self.table_list[i]}'
        except IndexError:
            pass
        for i in range(len(self.table_list), len(guests)):
            self.queue.put(guests[i])
            print(f'{guests[i]} встал(-а) в очередь')

    def discuss_guests(self):
        for table in self.table_list:
            if table.guest != None:
                table.guest.start()
        while not self.queue.empty():
            for table in self.table_list:
                if not table.guest.is_alive():
                    table.guest = self.queue.get()
                    print(f'{table.guest} сел(-а) за {table}')
                    table.guest.place = f'{table}'
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(guests)
# Обслуживание гостей
cafe.discuss_guests()