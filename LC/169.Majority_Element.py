# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:

# Input: nums = [3,2,3,3,4]
# Output: 3



def majorityElement(nums):
    counter = {}
    for i in nums:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i]+=1
    print(counter, "counter")
    print(counter.get, ".get")
    return max(counter, key=counter.get)

nums = [3,2,3,3,4]
print(majorityElement(nums))
