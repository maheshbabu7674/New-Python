# Polymorphism:  one thing have many forms

# Example:
# Shape----->circle,rectangle,square...
# polymorphism we can implement using overloading concept

# Example 1: polymorphism or overloading:

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")
h=Human()
h.sayhello("scott")
h.sayhello()               


#Example2:
class Calculation:
    def add(self, a=0,b=0,c=0):
        print(a+b+c)
calobj=Calculation()
calobj.add()        #0
calobj.add(10,20,30)  #60
calobj.add(10,20)    #30    
   
