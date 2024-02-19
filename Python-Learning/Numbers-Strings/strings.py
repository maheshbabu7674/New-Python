#Example 1
#create string variable
#Ways of creating string variable

s="welcome"
s='welcome'
s=str("welcome")
s=str('welcome')

#Creating empty string variable

name=""
name=''
name=str()

#Mutable ---Cannot change the value of the variable
#Immutable--Can change the value of variable

#Question
#1)Is strings are mutable ot immutable?
#Sol: Immutable

#Example 2:
#How to get the "id" of the variable memory

str1="welcome"
print(id(str1))           #1290623342448
str1=str1+"to python"
print(id(str1))            #2983438307504


#example 3:
# + and * with string

# + with string
str= "welcome"
print(str+"programming")

# * with string

print(str*3)

#Example 4:
# Slicing []

str = "welcome"
print(str[1:3])  #el  #starting index is '0': #ending index is '1'

#Example 5:
# ord() and chr()

print(ord("A"))
print(chr(65))

# Example 6: max(), min(), len()

print(max("welcome"))
print(min("welcome"))
print(len("welcome"))

# Example 7: in and not in operators---returns True/False:

s="welcome"

print("come" in s)      #True
print("lome" in s)      #False

print("come" not in s)  #False
print("lome" not in s)  #True

#Example 8:  String comparison

print("time"=="tie") # False
print("free"!="freedom") # True
print("arrow">"aron")# True
print("right">="left") #True
print("teeth"<"tee") #False
print("yellow"<="fellow") #False
print("abc">"") #True

# Example 9: Testing string->>True/False

s="welcome to python"
print(s.isalnum()) # False
print("welcome".isalpha()) #True
print("2024".isdigit()) #True
print("first number".isidentifier()) #False
print(s.islower()) # True
print("WELCOME".isupper()) #True
print(" ".isspace()) #True

#Example 10: Searching for substrings:

s="welcome to python"

print(s.endswith("thon")) # True
print(s.startswith("come")) # False
print(s.find("com")) #starting from 3rd place . So, it will give 3 
print(s.find("become")) # -1 not found
print(s.count("t")) # 2->Returns number of occurances of substrings the string

# Example 11:Converting string:

s="String in PYTHON"

s1=s.capitalize()
print(s1)  #String in python....(captalize means starting letter will be in Capital)
s2=s.title()
print(s2)  #String In Python
s3=s.lower()
print(s3)  #string in python
s4=s.upper()
print(s4) # STRING IN PYTHON
s5=s.swapcase()
print(s5) # sTRING IN python
s6=s.replace("in","on")
print(s6) #String on PYTHON

# Example 12: Reverse String:

# Method 1:
s="welcome"
rev_str=" "
for i in s:
    rev_str=i+rev_str
print("reversed string is:", rev_str) #emoclew

#Method2: using slicing operator

s="welcome"
rev_str=s[::-1] #s[0:6:-1]
print(rev_str) #emoclew

