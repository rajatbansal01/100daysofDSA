class Vehicle:

    def __init__(self, brand, name, color, wheels):
        self.brand = brand
        self.name = name
        self.color = color
        self.wheels = wheels


class Car(Vehicle):

    #   A car has always 4 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 4)


class Motorbike(Vehicle):

    #   A motorbike has always 2 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 2)

