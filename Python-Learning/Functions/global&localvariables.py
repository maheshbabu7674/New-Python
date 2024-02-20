# Example 1:

global_var = 20  #global variable

def func():
    local_var = 10
    print(local_var)
    print(global_var)
func()   #10    
         #20

#print(local_var)     # Invalid because local_var is local variable of func()

print(global_var)  #20, valid because global_var is global variable

# Example 2:
 
xy = 100  # global variable

def cool():
    xy=200          #local variable
    print(xy)
cool()  

print(xy)

# Example 3:

xy = 100  # global variable

def cool():
    global xy
    xy=234          #global variable
    print(xy)
cool()    #234
print(xy) #234

# Example 4:

def cool():
    global x
    x=100
    print(x)
cool()      #100
print(x)    #100  able to access 'x' beacuse it is global variable 

