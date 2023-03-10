"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import numpy as np
# create the prime sieve that we used in problem 3

upper_b = 1000000
nums = np.arange(2, upper_b)
primes = list()

while len(primes) < 10_001:
    primes.append(nums[0])
    nums = nums[nums % primes[-1] != 0]
print(len(primes))
print(primes[-1])

