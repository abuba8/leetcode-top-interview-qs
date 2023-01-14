def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    val = []
    # for ch1, ch2, ch3 in zip(nums, nums[1:], nums[2:]):
    #     # val.append(ch1, ch2, ch3)
    #     print(ch1,ch2,ch3)
    #     if ch1+ch2+ch3 == 0:
    #         val.append(sorted([ch1,ch2,ch3]))
    #     #     list.append([ch1, ch2, ch3])           
    #     # print(ch1, ch2, ch3)
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    val.append(sorted([nums[i], nums[j], nums[k]]))   
    
    print(set(val[0]))
    return val
        
x = threeSum([-1,0,1,2,-1,-4])
print(x)

