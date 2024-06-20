

class House:
    def __init__(self):
        self.number_OfFloors = 0

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print("Количество этажей в доме:", self.number_of_floors)

house = House()
house.set_new_number_of_floors(2)