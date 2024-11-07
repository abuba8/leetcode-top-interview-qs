class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val = int(''.join(str(x) for x in digits))
        return [int(x) for x in str(val+1)]
    
obj = Solution()
print(obj.plusOne([1,2,3]))
print(obj.plusOne([4,3,2,1]))
print(obj.plusOne([9]))