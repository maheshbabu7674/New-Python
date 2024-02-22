from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class Tiger(Animal):
    def eat(self):
        print("eat Non-Veg")
class Cow(Animal):
    def eat(self):
        print("eat Veg")

t=Tiger()
t.eat()

c=Cow()
c.eat()


