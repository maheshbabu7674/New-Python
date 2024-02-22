# open file and write the data into file:

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","w") #open file for writing

file.write("This is my first line\n")
file.write("This is my second line\n")

file.close()

#Reading all the data at once

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","r")
print(file.read()) # read entire content of the file at once
#print(file.read(10)) # read given number of characters from a file

file.close()

#readlines: all lines as an array

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","r")
print(file.readlines()) # read entire content of file at once in array format

file.close()

#output:
#['This is my first line\n', 'This is my second line\n']

#readline: reading only one line

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","r")
print(file.readline())  #read the first line

file.close()

# Output:
#This is my first line

# Appending data:

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","a") #open file for adding/appending

file.write("This is my third line\n")

file.close()


# Looping through the data using for loop:

file=open("C:/Users/jesus/OneDrive/Documents/pythonfilehandlingfile","r")

for l in file:
    print(l)
file.close()
