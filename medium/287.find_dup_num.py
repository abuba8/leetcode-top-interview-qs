class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapper = {}
        for i in range(len(nums)):
            if nums[i] not in mapper:
                mapper[nums[i]] = 1
            else:
                return nums[i]

obj = Solution()
print(obj.findDuplicate([1,3,4,2,2]))