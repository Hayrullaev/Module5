class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        for i in range(1, new_floor + 1):
            print(i)


house = House('ЖК Эльбрус', 22)
house.go_to(21)
house = House('Planeta', 4)
house.go_to(5)
