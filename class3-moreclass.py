class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self, human):
        self.passenger.append(human)

    def print_passenger(self):
        if self.passenger!=[]:
            print(f"Names of {self.brand} passenger:")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are no passenger in {self.brand}")

judi = Human("Judi")
person2 = Human("Jack")
car1 = Auto("Zaporozhets")
car2 = Auto("Porsche")

car1.print_passenger()
car2.print_passenger()
print("Go to car!")
car1.add_passenger(judi)
car1.add_passenger(person2)

car1.print_passenger()
car2.print_passenger()




