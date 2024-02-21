
import sys
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Packages/PackA")
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Packages/PackB")

# Approach 1:

import emp
empobj=emp.Employee(101,"John",5000000)
empobj.displayemp()

import stu
stuobj=stu.Student(3701,"Mahesh","B")
stuobj.displaystu()

# Output:
# 101 John 50000000
# 3701 Mahesh B

# Approach 2:

from emp import Employee
empobj=Employee(101,"John",50000000)
empobj.displayemp()

from stu import Student
stuobj=stu.Student(3701,"Mahesh","B")
stuobj.displaystu()

# Output:
# 101 John 50000000
# 3701 Mahesh B



