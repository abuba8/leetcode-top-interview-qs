def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    mapper = {}
    res = []
    for i, v in enumerate(nums):
        difference = target - v
        if difference in mapper:
            res.append(mapper[difference]+1)
            res.append(i+1)
            break
        else:
            mapper[v] = i
        
    print(res)

twoSum([2,7,11,15], 9)
twoSum([2,3,4], 6)