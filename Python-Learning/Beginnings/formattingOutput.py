#Formatting output

# Let's talk general way to print output

name = "john"
age = 30
sal = 500000

print(name)
print(age)
print(sal)

#Approach 1
name, age, sal ="John", 30, 55000.666
print(name,age,sal)

# Approach 2
print("Name is:",name)
print("Age is :",age)
print("Salary is :",sal)

# Approach 3 with % operator 
print("name is: %s Age is : %d Salary is : %g" %(name,age,sal))

# Approach 4 with {} operator
print("Name is :{} age is :{} salary is :{}" .format(name,age,sal))