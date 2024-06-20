class Building:
    def __init__(self, number_of_floors, building_Type):
        self.number_of_floors = number_of_floors
        self.building_Type = building_Type


    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors and self.building_Type == other.building_Type:
            return True
        else:
            return False


buiding1 = Building(6, 'Этажи ')
buiding2 = Building(5, 'Квартиры')
print(buiding1 == buiding2)
buiding1 = Building(4, 'Этажи')
buiding2 = Building(4, 'Квартиры')
print(buiding1 == buiding2)
