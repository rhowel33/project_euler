"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import numpy as np

nums = np.arange(1, 101)

sum_squared = np.sum(nums)**2

squares_summed = np.sum(nums**2)

print(sum_squared - squares_summed)