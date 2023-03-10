"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""

import numpy as np
one_to_twenty = np.arange(2, 21)
upper_b = np.prod(one_to_twenty)

nums = np.arange(100_000, 1_000_000_000,2)

for i in one_to_twenty:
    nums = nums[nums % i == 0]

print(nums[0])