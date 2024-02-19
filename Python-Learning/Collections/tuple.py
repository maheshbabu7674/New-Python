#Example1: How to create tuple and print

mytuple1=(10,20,30,40,50)
mytuple2=("apple","banana","cherry")
mytuple3=("apple",10,"banana",20,"cherry")
mytuple=()  ##Empty list

print(mytuple1)  #(10,20,30,40,50)
print(mytuple2)  #("apple","banana","cherry")
print(mytuple3)  #("apple",10,"banana",20,"cherry")
print(mytuple)   #()

#Example 2: Accessing items from the tuple:

mytuple=("apple","banana","cherry")  # Index starts from 0

print(mytuple[0])  #apple
print(mytuple[1])  #banana
print(mytuple[2])  #cherry
print(mytuple[-1]) #cherry
print(mytuple[-2]) #banana
print(mytuple[-3]) #apple

#Example 3:Range of indexes:

mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(mytuple[2:5])   #("cherry","orange","kiwi")
print(mytuple[-4:-1]) #("orange","kiwi","melon")

#Example 4: Change item value:

#by default tuple does not allow you chenge the values because it is immutable
# but there is work around by doing   tuple---->list(modify)---->tuple


mytuple=("apple","banana","cherry")
print(mytuple)   #("apple","banana","cherry")
mylist=list(mytuple)
print(mylist)   #['apple', 'banana', 'cherry']
mylist[0]="orange"
mytuple=tuple(mylist) 
print(mytuple)       #("orange","banana","cherry")

#Example5: Read the tuple items using loop:

mytuple=("apple","banana","cherry")
for i in mytuple:
    print(i)

#Example 6: Check if the item is exist in the tuple or not:

mytple=("apple","banana","cherry")   
if "apple" in mytuple:
    print("yes. apple is present")
else:
    print("no. apple is not present") 

#Example 7: tuple length(counting number of items in the tuple)

mytuple=("apple","banana","cherry")
print(len(mytuple))     # 3   

# Example 8: Add items to tuple-->not possible because tuple is immutable--->cannot change values/items

# mytuple=("apple","banana","cherry")
# mytuple[0]="orange" 
# print(mytuple)      #Type error: tuple object does not support item assignment

# Example 9: Copy tuple:

mytuple1=("apple","banana","cherry")
mytuple2=mytuple1
print(mytuple2)


# Example 10: Removing items from tuple --not possible because tuple is immutable

# mytuple=("apple","banana","cherry")
# mytuple.remove("apple") #invalid/it is not possible

#Example 11: Delete the tuple:

# mytuple=("apple","banana","cherry")
# del mytuple
# print(mytuple)  #NameError: name 'mytuple' is not defined. Did you mean: 'mytuple1'?

#Example 12: Join/combine tuple:

tuple1=(10,20,30)
tuple2=("a","b","c")
tuple3=tuple1+tuple2
print(tuple3)  #(10, 20, 30, 'a', 'b', 'c')

#Example 13: comparison:

tuple1=(10,20,30)
tuple2=("a","b","c")

if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")  #tuples are not equal  
