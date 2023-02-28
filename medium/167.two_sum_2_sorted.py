def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    mapper = {}
    res = []
    for i, v in enumerate(numbers):
        difference = target - v
        if difference in mapper:
            res.append(mapper[difference]+1)
            res.append(i+1)
            break
        else:
            mapper[v] = i
        
    return res