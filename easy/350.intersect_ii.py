def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if len(nums1) >= len(nums2):
        max_arr = nums1
        min_arr = nums2
    else:
        max_arr = nums2
        min_arr = nums1
        
    
    arr = []
    for x in min_arr: 
        if x in max_arr: arr.append(x)
            
    print(arr)

    
    # print(sorted(nums1), sorted(nums2))
    # for ch1, ch2 in zip(sorted(nums1), sorted(nums2)):
    #     print(ch1, ch2)
        
intersect([1,2,2,1], [2,2])
intersect([4,9,5], [9,4,9,8,4])
intersect([1,2,2,1], [2])
intersect([1,2], [1,1])