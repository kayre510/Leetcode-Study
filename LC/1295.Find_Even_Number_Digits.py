# Given an array nums of integers, return how many of them contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.


def findNumbers(nums):
    output = []
    for num in nums:
        if (len(str(num)) % 2 == 0):
            output.append(num)
    return len(output)
