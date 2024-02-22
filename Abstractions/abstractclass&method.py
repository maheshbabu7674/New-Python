from abc import ABC,abstractmethod
class A(ABC):  #ABC is pre-defined abstract class
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("this is display method")

obj=B()
obj.display()




