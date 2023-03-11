"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23]

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! 

[[75]
[95, 64]
[17, 47, 82]
[18, 35, 87, 10]
[20, 04, 82, 47, 65]
[19, 01, 23, 75, 03, 34]
[88, 02, 77, 73, 07, 63, 67]
[99, 65, 04, 28, 06, 16, 70, 92]
[41, 41, 26, 56, 83, 40, 80, 70, 33]
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
[04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23]]


"""
import numpy as np
# It seems that starting from the bottom would be advisable]

pyramid = [np.array([75]),
           np.array([95, 64]),
           np.array([17, 47, 82]),
           np.array([18, 35, 87, 10]),
           np.array([20,  4, 82, 47, 65]),
           np.array([19,  1, 23, 75,  3, 34]),
           np.array([88,  2, 77, 73,  7, 63, 67]),
           np.array([99, 65,  4, 28,  6, 16, 70, 92]),
           np.array([41, 41, 26, 56, 83, 40, 80, 70, 33]),
           np.array([41, 48, 72, 33, 47, 32, 37, 16, 94, 29]),
           np.array([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]),
           np.array([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]),
           np.array([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]),
           np.array([63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]),
           np.array([4., 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23])]

row_count = len(pyramid)
max_row = []
past_row = pyramid[-1]
for i in range(row_count - 2, 0, -1):
    print(past_row)
    print(pyramid[i])
    past_row = np.maximum(pyramid[i] + past_row[:-1],pyramid[i] + past_row[1:])
    print(past_row)
print(np.max(past_row) + pyramid[0][0])

