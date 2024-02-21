#Example 1:
 # Single Inheritance:

class A:            #parent class
    def m1(self):
        print('this is m1 method for class A')
class B(A):     #child class
    def m2(self):
        print("this is m2 method for class B")

bobj=B()
bobj.m1()
bobj.m2()

# output:
# this is m1 method for class A
# this is m2 method for class B

# Example 2:

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a-self.b)

bobj=B()     
bobj.m1()  # 30
bobj.m2()   # -100

#Example 3:
#Multi level Inheritance:

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=300,200
    def m2(self):
        print(self.a-self.b)

class C(B):
     i,j=5,2
     def m3(self):
         print(self.i*self.j)

cobj=C()
cobj.m1()   #30
cobj.m2()   #100
cobj.m3()   #10             

# Example 4:  Heirarchy Inheritance:

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=300,200
    def m2(self):
        print(self.a-self.b)

class C(A):
     i,j=5,2
     def m3(self):
         print(self.i*self.j)

bobj=B()
bobj.m1()  #30
bobj.m2()  #100

cobj=C()  
cobj.m1() #30
cobj.m3() #10

# Example 5: Multiple Inheritance:

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B():
    a,b=300,200
    def m2(self):
        print(self.a-self.b)

class C(A,B):
     i,j=5,2
     def m3(self):
         print(self.i*self.j)

cobj=C()
cobj.m1()   #30
cobj.m2()  #100
cobj.m3()   #10

# Example 6: Overriding method/concept:

class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m1(self):
        print("this is m1 method from class B")

bobj=B()
bobj.m1()      #this is m1 method from class B 

# without overriding the method
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1()  #to print parent class method through child class method

bobj=B()
bobj.m1()  #this is m1 method from class B
           #this is m1 method from class A

# Example 7:

class A:
    a,b=10,20

class B(A):
    i,j=100,200
    def m(self,x,y):
        print(x+y)  # local variables
        print(self.j+self.j)   # class B variables
        print(self.a+self.b)   # class A variables

bobj=B()
bobj.m(1000,2000)   

# output:

# 3000
# 400
# 30


# Example 8:

#How to overriding variables:

class Parent:
    name="scott"

class Child(Parent):
    name ="john"    #  overriding the variable value

cobj=Child()
print(cobj.name)  # john


# without overriding variables:

class Parent:
    name="scott"

class Child(Parent):
    name ="john"    
    def test(self):
        print(super().name)

cobj=Child()
print(cobj.name)  # john
cobj.test()  #scott


# Example 9: Overriding methods:

class Bank:
    def rateOfInterest(self):
        return 0
    
class XBank(Bank):
    def rateOfInterest(self):
        return 10
class YBank(Bank):
    def rateOfInterest(self):
        return 12     

objx=XBank()
print(objx.rateOfInterest()) #10

objy=YBank()
print(objy.rateOfInterest()) #12

#Example 10: Overloading 

   

