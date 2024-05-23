class House:
    def __init__(self):
        self.NumberOfFloors = 0

    def setNewNumberOfFloors(self,floors):
        self.NumberOfFloors = floors
        print('количество этажей в доме:',self.NumberOfFloors,)


ten_floor_house = House()

ten_floor_house.setNewNumberOfFloors(10)
print(ten_floor_house.NumberOfFloors)
