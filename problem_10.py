"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np

nums = np.arange(2, 2_000_000)
primes = list()

while len(nums > 0):
    primes.append(nums[0])
    nums = nums[nums % primes[-1] != 0]

print(np.sum(primes))
