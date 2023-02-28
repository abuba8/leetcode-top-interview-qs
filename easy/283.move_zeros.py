def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    for i in sorted(nums):
        if i == 0:
            nums.remove(i)
            nums.append(i)
            
    print(nums)
    
    
    
moveZeroes([0,1,0,3,12])
moveZeroes([0])