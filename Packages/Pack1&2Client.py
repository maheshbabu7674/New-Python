# Approach 1:
import sys
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Packages/Pack1")
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Packages/Pack1/Pack2")

import module1
import module2

module1.display()
module2.show()

#Output:
# This display function from module1
# This show function from module2

# Approach 2:

import sys
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Pack/Pack2")
sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Pack/Pack2/Pack2.0")

from module1 import *
from module2 import *

display()
show()

#Output:
# This display function from module1
# This show function from module2