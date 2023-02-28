def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)+1
    print(start,end)
    while start < end:
        mid = (start+end)//2
        if mid < target:
            
            start+=1
        else:
            end-=1
        
    print(start, end)
        


searchInsert([1,3,5,6], 5)
searchInsert([1,3,5,6], 2)
# searchInsert([1,3,5,6], 7)
