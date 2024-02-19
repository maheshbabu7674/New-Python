# Example1: Creating dictonary:

mydic={101:"x",102:"y",103:"z"}
print(mydic)               #{101: 'x', 102: 'y', 103: 'z'}

# Examle 2: Accessing items from dictonary:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

print(mydic["brand"])   #Hyundai
print(mydic["model"])   #i10
print(mydic["year"])    #2024

# using get() function:

x=mydic.get("brand")     #Hyundai
print(x)

#       0r

print(mydic.get("brand"))   #Hyundai

# Example 3: Change the values in dictonary:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

print(mydic)        #{'brand': 'Hyundai', 'model': 'i10', 'year': 2024}  
mydic["year"]=2023
print(mydic)        #{'brand': 'Hyundai', 'model': 'i10', 'year': 2023}

# Example 4: Reading items from dictonary using loop:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

for i in mydic:
    print(i)   #brand   ## prints only keys from dictonary
               #model
               #year

for i in mydic:
    print(mydic[i])    #Hyundai  ### prints only values from dictonary
                       #i10
                       #2024
    
for i in mydic.values():
    print(i)           #Hyundai  ### prints only values from dictonary
                       #i10
                       #2024
    
for x,y in mydic.items():
    print(x,y)        #brand Hyundai   ## Prints keys along with the values
                      #model i10
                      #year 2024

# Example 5: Check key is exist i dictonary or not:    

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

if "model" in mydic:
    print("exist")   # exist
else:
    print("not exist")    

    ## or
print("model" in mydic)   # True


# Example 6: Find the numbers of items in dictonary:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

print(len(mydic))  #3

# Example 7: Add items to dictonary:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

mydic["color"]="red"
print(mydic)      #{'brand': 'Hyundai', 'model': 'i10', 'year': 2024, 'color': 'red'}

# Example 8: Remove item from dictonary:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

# using pop() function:

# mydic.pop("year")
# print(mydic)       #{'brand': 'Hyundai', 'model': 'i10'}

# Using del:

del mydic["year"]
print(mydic)       #{'brand': 'Hyundai', 'model': 'i10'}

# delete complete dictonary:

# del mydic
# print(mydic)   #NameError: name 'mydic' is not defined

# to clear the dictonary:

mydic.clear()
print(mydic)   #{}

# Copy the item:

mydic1={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2024
}

# withour copy() function:
mydic2=mydic1
print(mydic2)   #{'brand': 'Hyundai', 'model': 'i10', 'year': 2024}

# Using copy() function:

mydic2=mydic1.copy()
print(mydic2)     #{'brand': 'Hyundai', 'model': 'i10', 'year': 2024}

