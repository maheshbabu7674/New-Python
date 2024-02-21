# same functions in 2 modules
# Approach 1:

import Animal
import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()
 
# Output

# Animal can't fly
# Animal color is black
# Bird can fly
# Bird color is yellow

# Approach 2:

from Animal import fly,color

fly()
color()

from Bird import fly,color

fly()
color()

# Output

# Animal can't fly
# Animal color is black
# Bird can fly
# Bird color is yellow

# Approach 3:

from Animal import *

fly()
color()

from Bird import *

fly()
color()

# Output

# Animal can't fly
# Animal color is black
# Bird can fly
# Bird color is yellow