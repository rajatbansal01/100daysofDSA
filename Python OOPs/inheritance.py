from abc import ABC, abstractmethod


#   Abstraction, this class cannot be instantiated.
class Vehicle(ABC):

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

    #   Polymorphism
    def description(self):
        return "I'm a vehicle."

    #   This method has to be implement in child classes.
    @abstractmethod
    def mileage(self):
        pass


class Car(Vehicle):

    #   A car has always 4 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 4)

    #   Polymorphism
    def description(self):
        return "I'm a car."

    def mileage(self):
        return "50kmph"


class Motorbike(Vehicle):

    #   A motorbike has always 2 wheels.
    def __init__(self, brand, name, color):
        super().__init__(brand, name, color, 2)

    #   Polymorphism
    def description(self):
        return "I'm a motorbike."

    def mileage(self):
        return "60kmph"
