"""
Original Code:
class Animal:
    def make_noise(self):
    print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
    print("Voff!")                     #not indented, error
class Cat(Animal):
    def make_noise(shelf):
    super().make_noise()
    print("Mjau!")

def sound_off(animal):                #error as it needs a loop to accommodate 3 elements of the list, c,d,h
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()                         #not define, error

sound_off([c, d, h])                  #list does not have make_noise(), error.
"""



class Animal:
    def make_noise(self):
       print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
       print("Voff!")                                #not indented earlier, error

class Cat(Animal):
    def make_noise(shelf):
       print("Mjau!")

class Rooster(Animal):
    def make_noise(shelf):
       print("Kuckeliku!")

def sound_off(animals):                #corrected to pass multiple animals
    for animal in animals:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()                         #not define earlier, error

sound_off([c, d, h])                  #list does not have make_noise(), error.