#Example 1:

def func(i,j):
    print(i,j)
#func(10,20)   #10 20  # positional arguments
func(j=20,i=10) #10 20 # keyword arguments


# Example 2: default values assigned to positional arguments:

def func(i,j=10):
    print(i,j)
#func(100,200)    #100 200
func(100)   # 100 10

# Example 3:

def greetings(name,greetmsg):
    print(greetmsg+" "+name)
greetings(name="Mahesh",greetmsg="hello")   #hello Mahesh
greetings(greetmsg="hello",name="Mahesh")  #hello Mahesh

# Example 4: Combination of positional and keyword arguments:

def my_fun(a,b,c):
    print(a,b,c)

my_fun(10,20,30)        # 10 20 30 positional arguments
my_fun(a=10,b=20,c=30)  # 10 20 30 keyword arguments
my_fun(b=20,a=10,c=30)  # 10 20 30 keyword arguments

my_fun(10,20,c=30)      # 10 20 30(combination of positional arguments and positional arguments)
my_fun(10,b=20,c=30)    # 10 20 30(combination of positional arguments and positional arguments)
#my_fun(10,b=20,30)  # This is wrong as positional argument must appear before any keyword argument
                     #SyntaxError: positional argument follows keyword argument
#my_fun(10,20,b=20)   # Thais is having logical error #TypeError: my_fun() got multiple values for argument 'b'


#Exampple 5:

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(10,20))   #(20, 10) 
print(largest(200,100)) #(200,100)

##  or ###

result=largest(10,20)
print(result)

print(type(result))  #<class 'tuple'>  ()


