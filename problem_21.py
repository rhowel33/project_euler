"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a)= b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
import numpy as np

ranges = (2, 10001)


def d(n):
    divisors = set()
    for i in range(1, int(n)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    divisors.remove(n)
    return int(sum(list(divisors)))


div_sums = {i:d(i) for i in range(*ranges)}
ami_nums = []
for a in range(*ranges):
    try:
        b = div_sums[a]
        if div_sums[b] == a and a != b:

            ami_nums.append(a)
    except KeyError:
        pass

print(np.sum(ami_nums))
