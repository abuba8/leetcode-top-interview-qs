def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    for x in range(len(nums)):
        for j in range(x+1, len(nums)):
            if nums[x] == nums[j]:
                temp = nums[x]
            
            # if temp == x:
            #     temp = x
            # else:
            #     continue
        
    print('temp', temp)

findDuplicate([1,3,4,2,2])