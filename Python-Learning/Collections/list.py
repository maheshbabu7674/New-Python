#Example1: How to create list and print

mylist1=[10,20,30,40,50]
mylist2=["apple","banana","cherry"]
mylist3=["apple",10,"banana",20,"cherry"]
mylist=list()  ##Empty list

print(mylist1)  #[10,20,30,40,50]
print(mylist2)  #["apple","banana","cherry"]
print(mylist3)  #["apple",10,"banana",20,"cherry"]
print(mylist)   #[]


#Example 2: Accessing items from the list:

mylist=["apple","banana","cherry"]  # Index starts from 0

print(mylist[0])  #apple
print(mylist[1])  #banana
print(mylist[2])  #cherry
print(mylist[-1]) #cherry
print(mylist[-2]) #banana
print(mylist[-3]) #apple


#Example 3:Range of indexes:

mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(mylist[2:5])   #["cherry","orange","kiwi"]
print(mylist[-4:-1]) #["orange","kiwi","melon"]

#Example 4: Change item value:

mylist=["apple","banana","cherry"]
print(mylist)   #["apple","banana","cherry"]
mylist[0]="orange" #This will change the values based on index
print(mylist)   #['orange', 'banana', 'cherry']

#Example5: Read the list items using loop:

mylist=["apple","banana","cherry"]
for i in mylist:
    print(i)

#Example 6: Check if the item is exist in the list or not:

mylist=["apple","banana","cherry"]   
if "apple" in mylist:
    print("yes. apple is present")
else:
    print("no. apple is not present") 

#Example 7: List the length(counting number of items in the list)

mylist=["apple","banana","cherry"] 
print(len(mylist))     # 3

#Example 8: 
# 1). Add items in the existing list using append() function

mylist=["apple","banana","cherry"] 
mylist.append('orange') # adding new item at the end of the list
print(mylist)           #['apple', 'banana', 'cherry', 'orange']

# 2). Insert item in the existing list using insert() function

mylist=["apple","banana","cherry"] 
mylist.insert(2,'orange') #Add/insert the item in the list based on index
print(mylist)             #['apple', 'banana', 'orange', 'cherry']

# Example 9: Remove item from the list 

# 1).using pop() function

mylist=["apple","banana","cherry"] 
mylist.pop(2)      #here we should specify index not the value
print(mylist)      # ['apple', 'banana']

# 2). Using del keyword

mylist=["apple","banana","cherry"]

del mylist[1] # here del command removes single item based on the index
print(mylist)  #['apple', 'cherry']

# 3). Using clear() function

mylist=["apple","banana","cherry"] 
mylist.clear()  #It will delete/remove/clear all items in the the list 
print(mylist)   #[]

# Example 10: Copy list:

# Approach 1: using list() function:

mylist1=["apple","banana","cherry"]
mylist2=list(mylist1)
print(mylist1)
print(mylist2)

# Approach 2: Using copy() function:

mylist1=["apple","banana","cherry"]
mylist2=mylist1.copy()
print(mylist1)
print(mylist2)

# Example 11: Combine/join items:

# Using + operator

list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)      #['a', 'b', 'c', 1, 2, 3]

# Using loop statement:

list1=['a','b','c']
list2=[1,2,3]
for i in list2:
    list1.append(i)
print(list1) 

# Using exatend() function:

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)


#Example 12: comparison:

list1=[10,20,30]
list2=["a","b","c"]

if list1==list2:
    print("lists are equal")
else:
    print("lists are not equal")  #list are not equal 

