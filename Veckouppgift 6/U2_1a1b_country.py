#1a Added objects from Iceland and denmark population to the class
#1b Added a method to print the population per country.



class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop


    def print_info(self):                                    #1b added print_info method
        print(f"There are {self.__population} million inhabitants in {self.__name}.")


se = Country("Sweden", 10.5)
no = Country("Norway", 5.5)
isl = Country("Iceland", 0.4)                                #1a added object Iceland
dk = Country("Denmark", 0.6)                                 #1a added object Iceland

se.print_info()
no.print_info()
isl.print_info()
dk.print_info()

