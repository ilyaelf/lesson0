from threading import Thread
import time

class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        while True:
            enemy -= self.power
            day +=1
            print(f'{self.name} сражается {day} дней, оталось {enemy} врагов\n')
            time.sleep(1)
            if enemy <= 0:
                print(f'{self.name} победил спустя {day} дней\n')
                break

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("все битвы закончились")