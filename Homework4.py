class Building:
    total = 0

    def __init__(self):
        Building.total += 1

if __name__ == '__main__':
    for i in range(40):
        building = Building()
        print(f'Создан объект {building}')
    print(f'{Building.total} объектов создано')