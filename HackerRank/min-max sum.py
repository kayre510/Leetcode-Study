# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# arr = [1,3,5,7,9]
# The minimum sum is 1+3+5+7=16  and the maximum sum is 3+5+7+9=24. The function prints 16 24


import math

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[-4:])
    print(min_sum, max_sum)

