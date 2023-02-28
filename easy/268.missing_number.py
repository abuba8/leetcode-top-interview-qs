def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    for i in range(len(nums)):
        if i not in nums:
            return i
    
    return len(nums)

    
x = missingNumber([3,0,1])
print(x)
x = missingNumber([0,1])
print(x)
x = missingNumber([9,6,4,2,3,5,7,0,1])
print(x)
