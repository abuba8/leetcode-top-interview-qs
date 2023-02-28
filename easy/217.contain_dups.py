def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    if len(nums) == len(set(nums)):
        return False
    else:
        return True
    
    
    
x = containsDuplicate([1,2,3,1])
print(x)
x = containsDuplicate([1,2,3,4])
print(x)
x = containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(x)