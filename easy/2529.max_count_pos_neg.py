def maximumCount(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    print(nums)
    pos, neg = 0, 0
    for x in nums:
        if x > 0:
            pos += 1
        if x < 0:
            neg += 1
    
    return max(pos, neg)
    
    
maximumCount([-2,-1,-1,1,2,3])
maximumCount([-3,-2,-1,0,0,1,2])
maximumCount()