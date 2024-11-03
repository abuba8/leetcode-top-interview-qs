class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)

obj = Solution()
print(obj.removeElement([3,2,2,3], 3))
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))