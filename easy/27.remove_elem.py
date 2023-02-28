def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    print(len([x for x in nums if x != val]))
    # print(nums)


removeElement([3,2,2,3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)