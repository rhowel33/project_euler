"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a)= b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
import numpy as np


def d(n):
    divisors = set()
    for i in range(1, int(n)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return int(sum(list(divisors.remove(n))))

sums = np.array([1]+[d(i) for i in range(2, 10001)])
# print(sums)
total_sum = 0

for i, sum1 in enumerate(sums):
    print(i,sum1)
    if sums[sum1] == i and i != sum1:
        total_sum += i
        print(i)

print(f'final sum is {total_sum}')