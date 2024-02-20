# Example 1:
 #Declaring the function:

def myfun():
    print("hello")

# Calling the function:
    
myfun()    #hello

# Example 2:

def myfun(name):
    print("hello",name)

myfun("mahesh")        #hello mahesh

# Example 3:

def cal(a,b):
    return(a+b)

sum=cal(100,200)
print(sum)

##   or    ##

print(cal(10,20))


# Example 4:

def func():
    return

func()

##  or  ##

print(func())  ## None

# Example 5:

def cal(a,b):
    print(a+b)
cal(10,20)  #30

  ## or   ##

def cal(a,b):
    return(a+b)
print(cal(1,20)) #21    