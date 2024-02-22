# Example 1: # private variables can be access only with in the class:

class myclass:
    __a=10
    def display(self):
        print(self.__a)

obj=myclass()
obj.display()

#print(myclass.__a) # we cannot access because it is private #AttributeError: type object 'myclass' has no attribute '__a'

# Example 2:#Private methods can be access only within the nethod

class myclass:
    def __display(self):  # private method
        print("this is private diplay method ")
    def display2(self):
        print("this is display method")
        self.__display()
obj=myclass()
#obj.__display()  #not correct
obj.display2()


#Example 3:

# can access private variable outside of class indirectly using methods:

class myclass:
    __empid=105

    def getempid(self,eid):
        self.__empid=eid
    def dispempid(self):
        print(self.__empid)

obj=myclass()
obj.getempid(104)
obj.dispempid()
