# How to call the functions from one module to another module
# Approach 1:

import Calculator
Calculator.add(100,200)
Calculator.mul(10,20)

# Output:
# 300
# 200

# Approach 2:

from Calculator import add,mul
add(100,200)
mul(10,20)

# Output:
# 300
# 200

# Approach 3:

from Calculator import *
add(100,200)
mul(10,20)

# Output:
# 300
# 200