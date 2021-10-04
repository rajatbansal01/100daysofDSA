class Vehicle:

    def __init__(self, brand, name, color, wheels):
        self.brand = brand

        #   Encapsulation protected variable, Vehicle, Car and Motorbike can access this variable.
        self._name = name

        #   Encapsulation private variable, only Vehicle class can access this variable.
        self.__color = color
        self.wheels = wheels

    #   A way to expose a private variable so it can be read by others but it still can't be modified
    #   from outside the class.
    def get_color(self):
        return self.__color


class Car(Vehicle):

    #   A car has always 4 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 4)


class Motorbike(Vehicle):

    #   A motorbike has always 2 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 2)

