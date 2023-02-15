def smallerNumbersThanCurrent(nums):
    mydict = dict()
    for k, v in enumerate(sorted(nums)):
        if v not in mydict:
            mydict[v] = k
    return [mydict[item] for item in nums]



nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))
