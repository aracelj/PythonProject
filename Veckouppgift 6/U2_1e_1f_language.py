#1e Added a method to add_language
#1f Update print_info to add language in new line.



class Country:
    def __init__(self, name, pop, area=None, languages=None):       #objects
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = languages


    def print_info(self):
        if self.__area is not None:                                 #added area condition to print
            print(f"There are {self.__population} million inhabitants in {self.__name} with an area of {self.__area} km².")
        else:
            print(f"There are {self.__population} million inhabitants in {self.__name}")

        if self.__languages is not None:                            #added language condition to print in another line
            add_languages = ", ".join(self.__languages)
            print(f"Official Languages: {add_languages}")


se = Country("Sweden", 10.5, 450295, ["Swedish"])
fi = Country("Finland", 5.6, 338145, ["Finnish", "Swedish", "Sámi"])
ch = Country("Switzerland", 9.1, 41285, ["German", "French", "Italian", "Romansh"])


countries = [se, fi, ch]
for country in countries:
    country.print_info()





