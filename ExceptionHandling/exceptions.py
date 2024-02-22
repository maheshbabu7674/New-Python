# Example 1:

print("Initializing the program")
print("Started the program")
print("Program is in progress")

try:
    print(x)
except:
    print("Exception occured")

print("Program is running")
print("Program ended")

#Output:

# Initializing the program
# Started the program
# Program is in progress
# Exception occured
# Program is running
# Program ended

# Example 2:

print("Initializing the program")
print("Started the program")
print("Program is in progress")
print(10/5)                    #2.0
print("Program is running")
print("Program ended")

print("Initializing the program")
print("Started the program")
print("Program is in progress")
#print(10/0)                    #ZeroDivisionError: division by zero
print("Program is running")
print("Program ended")

# To overcome above one we need to use exception handling:

print("Initializing the program")
print("Started the program")
print("Program is in progress")
try:
    print(10/0)
except ZeroDivisionError:  # if you know exception then use like this
    print("Exception occured ...hanled..")
print("Program is running")
print("Program ended")

# Example 3:
#Multiple Except blocks--try, except, else, finally

print("Initializing the program")
print("Started the program")
print("Program is in progress")
try:
    print(10/0)
except:  # if you know exception then use like this
    print("Exception occured ...hanled..")
#except:  # if you know exception then use like this
#    print("Exception occur ...hanld..")
else:
    print("Entered into else block...")
finally:
    print("Entered into finally block..")

print("Program is running")
print("Program ended")

# case 1: Thrown exception ---->except
#case 2: Not thrown exception --->else (executed only if the statement ot thrown any exception)
