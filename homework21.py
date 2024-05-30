class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000

    def horsepowers(self):
        print('мощность',100)

class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = 'car'

    def horsepowers(self):
        print('мощность',140)


teana = Nissan()
print(teana)
print("тип", teana.vehicle_type, "цена", teana.price)
teana.horsepowers()