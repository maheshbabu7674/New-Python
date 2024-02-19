# if, if ..else, elif

#Example 1
#Print a person is eligible for vote or not.
# age>=18

# age =15

# if age>=18:
#     print("Eligible for vote")

# else:
#     print("Not eligible for vote")    


# #Example 2

# if True:
#     print("true condition")

# else:
#     print("false condition")  

# ## (or) ##

# if False:
#     print("true condition")

# else:
#     print("false condition")      

# #Example 3

# if 1:
#     print("one")
# else:
#     print("not one")            

# Example 4
# Find a number is even/odd num

# num=9
# if num%2==0:
#     print("Given number is even")
# else:
#     print("Given number is odd")    

#Example 5:
    #if else in single line (ternary operator)
num=10
print("Given number is even") if num%2==0 else print("Given number is odd")

# #Example 6:

#if else---multiple statements in single line

# a=20

# {print("hello"),print("python")} if a>=10 else{print("hi"),print("java")}

#Example 7:
#Multiple conditions using "elif"

# weekno=4
# if weekno==1:
#     print("Sunday")
# elif weekno==2:
#     print("Monday") 
# elif weekno==3:
#     print("Tuesday") 
# elif weekno==3:
#     print("Wednesday") 
# elif weekno==4:
#     print("Thursday")         
# elif weekno==5:
#     print("Friday") 
# elif weekno==6:
#     print("Saturday") 
# else:
#     print("Invalid Week no")  

#1) Check the given is positive or negitive:

# a=-1
# if a>0:
#     print("Positive number")
# else:
#     print("Negitive number")           

#2) Check the largest of 2 numbers

# a=200
# b=300

# if b>a:
#     print("Largest")
# else:
#     print("Not Largest")  

# Python Program to find Largest of Two Numbers

# a = float(input(" Please Enter the First Value a: "))
# b = float(input(" Please Enter the Second Value b: "))

# if(a > b):
#     print("{0} is Greater than {1}".format(a, b))
# elif(b > a):
#     print("{0} is Greater than {1}".format(b, a))
# else:
#     print("Both a and b are Equal")      

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# print weekno if you provide week name as input