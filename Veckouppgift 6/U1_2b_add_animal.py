# Added parrot sound to the existing code in 2a


class Animal:
    def make_noise(self):
       print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
       print("Voff!")

class Cat(Animal):
    def make_noise(self):
       print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
       print("Kuckeliku!")

class Parrot(Animal):                                        #adding parrot to the class
    def make_noise(shelf):
       print("Hello!")

def sound_off(animals):
    for animal in animals:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
i = Parrot()#not define earlier, error

sound_off([c, d, h, i])
