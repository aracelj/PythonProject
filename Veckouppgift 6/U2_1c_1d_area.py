#1c Added object area to the class
#1d Added a method to print the area parameter per country


class Country:
    def __init__(self, name, pop, area=None):                       #added method for area
        self.__name = name
        self.__population = pop
        self.__area = area


    def print_info(self):
        if self.__area is not None:                                 #added area condition to print
            print(f"There are {self.__population} million inhabitants in {self.__name} with an area of {self.__area} km².")
        else:
            print(f"There are {self.__population} million inhabitants in {self.__name}")


se = Country("Sweden", 10.5, 450295)
no = Country("Norway", 5.5, 385207)
isl = Country("Iceland", 0.4, 103000)
dk = Country("Denmark", 0.6)

se.print_info()
no.print_info()
isl.print_info()
dk.print_info()



