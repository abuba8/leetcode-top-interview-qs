def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    final_nums = sorted(nums1 + nums2)
    if len(final_nums) % 2 == 0:
        mid_index_1 = len(final_nums) // 2 - 1
        mid_index_2 = mid_index_1 + 1
        print(float((final_nums[mid_index_1]+final_nums[mid_index_2])/2) )
        return float((final_nums[mid_index_1]+final_nums[mid_index_2])/2) 
    else:
        mid_index = len(final_nums) // 2
        print(float(final_nums[mid_index]))
        return float(final_nums[mid_index])