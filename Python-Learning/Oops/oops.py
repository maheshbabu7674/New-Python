# Example 1:

class Myclass:    # class
    def myfun(self):
        pass
    def display(self):
        print("john")
mc1=Myclass()       # object
mc1.myfun()
mc1.display()    #john

##  or  ##
class Myclass:
    def myfun(self):
        pass
    def display(self,name):
        print(name)
mc1=Myclass()
mc1.myfun()
mc1.display("scott") #scott

# Example 2:

class Myclass:
    def m1(self):
        print("this is instance method...")
    @staticmethod
    def m2(self,num):
        print(self,num) 
mc=Myclass()
mc.m1()
mc.m2(109,890)    #109 890
Myclass.m2(10,20)  #  10 20    (This is recommended one) Here we are calling static method directly using class not through object




# Example 3:
# Class variables:
class Myclass:
    a,b=10,20  # class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
mc=Myclass()
mc.add()  #30
mc.mul()  #200 

# Example 4:
#Combination of local, class and global variables;

i,j=15,20      #global variables
class Myclass:
    a,b=10,20   # class variables
    def add(self,x,y):
        print(x+y)    #x,y are local variables
        print(self.a+self.b)  #a,b are class variables
        print(i+j)  #i,j are global variables
mc=Myclass()
mc.add(300,400)        

# Output:
#700
#30
#35

# Example 5:

a,b=15,20      #global variables
class Myclass:
    a,b=10,20   # class variables
    def add(self,a,b):
        print(a+b)    #a,b are local variables
        print(self.a+self.b)  #a,b are class variables
        print(globals()['a']+globals()['b'])  #a,b are global variables
mc=Myclass()
mc.add(300,400)  

#Output:
#700
#30
#35

# Example 6: One class can have multiple objects:

class Myclass:
    def display(self,name):
        print("this is display method..")
        print(name)
obj1=Myclass()
obj1.display("john")

obj2=Myclass()
obj2.display("scott")

# output:
# this is display method..
# john
# this is display method..
# scott

#Example 7:

#Constructor:

class Myclass:
    def __init__(self):
        print("this is consructor..")
    def m1(self):
        print("hello..")
    def m2(self,x,y):
        return(x+y)    
mc=Myclass()         #this is consructor..  #  Invoke constructor automatically
mc.m1()              #hello..     #method we have call explicitely by using object
print(mc.m2(15,60))   #75

# Example 8:

class Myclass:
    name="john"
    def __init__(self,name):   # constructor expecting one argument
        print(name)
        print(self.name)
mc=Myclass("David")    #passing parameter to the constructor 


# Example 9:

