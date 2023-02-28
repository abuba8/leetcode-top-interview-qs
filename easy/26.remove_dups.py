def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = list(sorted(set(nums)))
    
    
    
removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])