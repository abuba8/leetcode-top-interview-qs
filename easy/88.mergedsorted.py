class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1[:] = nums2[:n]
        elif n == 0:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = nums1[:m] + nums2[:n]
            nums1[:] = sorted(nums1)

        return nums1

obj = Solution()    
print(obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(obj.merge([1], 1, [], 0))
print(obj.merge([0], 0, [1], 1))
