"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import numpy as np

# create a function that can recognise palindromic numbers
def is_palindrome(n):
    """
    checks to see if n (int) is a palindromic number
    returns True or False
    """

    return str(n) == str(n)[::-1]

# create the list of numbers to loop through
nums = np.arange(999, 99, -1)

# set a variable for largest
largest = 0


# start the loop
for i in nums:
    for j in nums:
        if i < j:
            pass
        else:
            n = i*j
            if is_palindrome(n) and n > largest:
                largest = n

print(largest)

