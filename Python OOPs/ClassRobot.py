class Robot:
 
    def __init__(self, name=None, build_year=None):
        self.__name = name
        self.__build_year = build_year
        
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
# Using the setter and getter method          
    def set_name(self, name): # Setter method is used to set the value.
        self.__name = name
        
    def get_name(self): # getter method is used to get the value.
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year    
    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)

# Driver code     
if __name__ == "__main__":
    x = Robot("Umakshi", 2002)
    y = Robot("Sophia", 2012)
    for rob in [x, y]:
        rob.say_hi()
        print("I was built in the year " + str(rob.get_build_year()) + "!")


