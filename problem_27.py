"""
Euler discovered the remarkable quadratic formula: n^2 + n + 41.

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when  n = 40, 40^2 + 40 + 41 = 40 ( 40 + 1) + 41 is divisible by 41, and certainly when
 n = 41, 41^2 + 41 + 41  is clearly divisible by 41.

 The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive
 values  0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479

 Considering quadratics of the form:
 n^2 + a*n + b , where  |a| < 1000  and  |b| ≤ 1000
where |n|
 is the modulus/absolute value of n

e.g. |11|=11 and |-4| = 4.

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.
"""
import numpy as np

# create a prime seive and a list of the primes
upper_b = 1000000
nums = np.arange(2, upper_b)
primes = list()

while len(primes) < 10_001:
    primes.append(nums[0])
    nums = nums[nums % primes[-1] != 0]

form = lambda x,y,n: n**2 + x*n + b
max_count = 0
product = 0
for a in range(1000, -1000, -1):
    for b in range(1000, -1000, -1):
        n = 0
        count = 0
        while form(a,b,n) in primes:
            n += 1
            count += 1
        if count > max_count:
            max_count = count
            product = a * b

print(product)

