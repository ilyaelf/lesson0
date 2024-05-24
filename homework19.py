class Building:
    total = 0
    name = ""
    
    def __init__(self,i):
        self.name = 'building_№'+str(i+1)
        self.total = 1+i
        Building.total = Building.total + 1

    def __str__(self):
        return f'{self.name}'


for i in range(40):
    building = Building(i)
    print(building)

print('building count',Building.total)
