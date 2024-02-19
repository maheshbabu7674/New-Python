# Example1: creating set:

myset={"apple","banana","cherry"}
print(myset)            #{'apple', 'cherry', 'banana'}

# Example 2: Accessing the items from set:

myset={"apple","banana","cherry"}

for i in myset:
    print(i)


# Example 3:  Value/item exists in set or not:
    
myset={"apple","banana","cherry"}

print("banana" in myset)   #True
print("orange" in myset)   #False

# Example 4: Adding items to set:

# add()  -----> we can add single item with using add() function:

myset={"apple","banana","cherry"}

myset.add("orange")
print(myset)    #{'orange', 'apple', 'banana', 'cherry'}

# update()  -----> we can add multiple items with using update() function:

myset={"apple","banana","cherry"}

myset.update(["orange","grapes","mahesh"])
print(myset)    #{'orange', 'grapes', 'apple', 'mahesh', 'banana', 'cherry'}

# Example 5: How to find number of items in set:

myset={"apple","banana","cherry"}

print(len(myset))  # 3


# Example 6:  How to remove the items from  set:


# with remove()function:

myset={"apple","banana","cherry"}

myset.remove("banana")
print(myset)    #{'apple', 'cherry'}

# myset.remove("xyz")   #KeyError: 'xyz'

# With discard():

myset={"apple","banana","cherry"}

myset.discard("banana")
print(myset)    #{'apple', 'cherry'}

myset.discard("xyz")   # will not through any errror

# Example 7: How to clear items from set:

myset={"apple","banana","cherry"}

# myset.clear()
# print(myset) 

#del myset
# print(myset)   #NameError: name 'myset' is not defined

# Example 8: Joining 2 sets:

# By using union() function:

set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)

print(set3)  #{1, 2, 3, 'b', 'a', 'c'}

# By using update() function:

set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)

print(set1)










