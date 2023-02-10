# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    # create an empty dictionary to hold the values
    #create an empty array to hold the indexes of the values
    #iterate through nums using enumerate to grab each index and value within nums
    #set needed value = target - nums
    #if needed value is in dictionary
    #output.append[i]
    #else dictionary[]

    dictionary = {}
    output = []
    # for i, j in enumerate(nums):
    #     needed_value = target - j
    #     if needed_value in dictionary:
    #         output.append[i]
    #     else:
    #         dictionary[i] = needed_value
    for index, value in enumerate(nums):
        needed_value = target - value
        if needed_value in dictionary:
            output.append(dictionary[needed_value])
            print(dictionary[needed_value])
            output.append(index)
            return output
        else: dictionary[value] = index

#dictionary = {value: index}

print(twoSum([1,4,6,9], 13))

