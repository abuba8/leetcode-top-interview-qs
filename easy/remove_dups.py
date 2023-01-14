def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique_elems = list(set(nums))
    n = len(nums)
    final_nums = [None] * n
    
    for i in range(n):
        if i < len(unique_elems):
            final_nums[i] = unique_elems[i]
            
    print(final_nums)
    
    
removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])