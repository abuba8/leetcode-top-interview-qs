class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # print(dividend, divisor)
        print(int(dividend/divisor))
    
obj = Solution()
print(obj.divide(10, 3))
print(obj.divide(7, -3))