def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    mapper = {}
    for i in nums:
        mapper[i] = mapper.get(i, 0) + 1
    
    for i, v in enumerate(mapper):
        if mapper.get(v) == 1:
            return v    
    
        
singleNumber([2,2,1])
singleNumber([4,1,2,1,2])
singleNumber([1])
