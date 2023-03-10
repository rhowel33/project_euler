"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 ==> 9+ 16 + 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import numpy as np

# create a list of squares
nums = np.arange(1, 31)
squares = nums ** 2



# create a 2dim matrix
for a in range(1, 500):
    for b in range(1, 500):
        if a >= b:
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                print(a*b*c)

