import sys

sys.path.append("C:/Users/jesus/Downloads/git-repo/Github/New-Python/Pack/Pack1")

# Approach 1:

import module1
import module2

module1.display()
module2.show()

# Approach 2:

from module1 import *
from module2 import *

display()
show()