def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    if m == 0:
        return sorted(nums2[:n])
    elif n == 0:
        return sorted(nums1[:m])
    else:
        val = nums1[:m] + nums2[:n]
        return sorted(val)
x = merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(x)
x = merge([1], 1, [], 0)
print(x)
