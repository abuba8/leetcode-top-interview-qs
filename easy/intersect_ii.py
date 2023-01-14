def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    print(sorted(nums1), sorted(nums2))
    for ch1, ch2 in zip(sorted(nums1), sorted(nums2)):
        print(ch1, ch2)
        
intersect([1,2,2,1], [2,2])
# intersect([4,9,5], [9,4,9,8,4])