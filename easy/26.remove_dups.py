class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Alternate Solution: 
        nums[:] = list(sorted(set(nums)))
        '''

        if len(nums) < 2: return len(nums)
        else:
            i = 0
            j = 0
            while i < len(nums):
                if nums[i] == nums[j]: i+=1
                else:
                    j+=1
                    nums[j] = nums[i]
                    i+=1
            return j+1

        

obj = Solution()
print(obj.removeDuplicates([1,1,2]))
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))