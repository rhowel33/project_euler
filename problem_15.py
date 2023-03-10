"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


"""

import numpy as np
x = 4
# create the grid
grid = np.array([[2 if i < x-1 and j < x-1 else 1 for i in range(x)] for j in range(x)])
print(grid)