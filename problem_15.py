"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


"""

import numpy as np
from math import comb
# we need a path length of 40
# and we now it has to come from a combination of 20


print(comb(40, 20))
