class Building:
    def __init__(self,NumberOfFloors,BuildingType):
        self.NumberOfFloors = NumberOfFloors
        self.BuildingType = BuildingType

    def __eq__(self, other):
        return ((self.BuildingType == other.BuildingType)
                and (self.NumberOfFloors == other.NumberOfFloors))

house1 = Building(42,'weed')
house2 = Building(1,'wood')

if house1 == house2:
    print('True')
else:
    print('False')



