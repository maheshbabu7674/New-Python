import sys

sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Packages/SamplePack")

# Approach 1:

import module1
import module2

module1.display()
module2.show()

#Output:
# This display function from module1
# This show function from module2

# Approach 2:

from module1 import *
from module2 import *

display()
show()

#Output:
# This display function from module1
# This show function from module2