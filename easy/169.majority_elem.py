def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    mapper = {}
    n = len(nums)
    for i in nums:
        mapper[i] = mapper.get(i, 0) + 1
    
    for i, v in enumerate(mapper):
        if mapper.get(v) > (n/2):
            return v  
    
    
majorityElement([3,2,3])
majorityElement([2,2,1,1,1,2,2])