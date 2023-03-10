"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import numpy as np

# find the upper bound by taking the sqrt
target = 600851475143
upper_b = int(np.sqrt(target))

# create a prime sieve up to the upper_b
nums = np.arange(2, upper_b)
primes = list()

while len(nums > 0):
    primes.append(nums[0])
    nums = nums[nums % primes[-1] != 0]

# flip the order of the array, so we start from the largest value
primes.reverse()
for i in primes:
    if target % i == 0:
        print(f"{i} is the largest prime factor")
        break