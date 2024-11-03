class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        mapper = {}
        for i, v in enumerate(nums):
            if target - nums[i] in mapper:
                return (mapper[target-nums[i]], i)
            mapper[nums[i]] = i

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))
print(obj.twoSum([3,2,4], 6))