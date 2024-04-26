class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self , floors):
        self.numberOfFloors = floors
        print(f'Теперь в доме {self.numberOfFloors} этажей')


my_house = House()
my_house.setNewNumberOfFloors(10)
my_house.setNewNumberOfFloors(15)
my_house.setNewNumberOfFloors(20)