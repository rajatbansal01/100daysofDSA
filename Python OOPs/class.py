#   All definitions can be found in the readme.

#   Class
class Car:

    #   Constructor
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    #   Methods
    #   With parameters.
    def max_speed(self, max_speed):
        return f"Max speed is {max_speed}"

    #   Without parameters
    def full_name(self):
        return f'{self.brand - self.name}'


#   Object instantiation.
fiat = Car("Fiat",  "500", "white")
honda = Car("Honda", "Civic", "black")

