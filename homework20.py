class Car:
    price = 1000000

    def horsepowers(self):
        print('мощность',100)

class Nissan(Car):
    price = 2000000
    def horsepowers(self):
        print('мощность 130')

class Kia(Car):
    price = 1900000

    def horsepowers(self):
        print('мощность 140')


randomcar = Car()
randomcar.horsepowers()
print(randomcar.price)
almera = Nissan()
almera.horsepowers()
print(almera.price)
cerato = Kia()
cerato.horsepowers()
print(cerato.price)