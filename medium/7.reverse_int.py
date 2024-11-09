class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        rev = 0
        m = x
        if m < 0: x = x * -1
        
        while(x > 0):
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
        
        if m < 0: 
            if rev >= -2 ** 31 and rev <= (2 ** 31)-1:
                return rev * -1
            else:
                return 0
        
        if rev >= -2 ** 31 and rev <= (2 ** 31)-1:
            return rev
        else:
            return 0

obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
print(obj.reverse(1534236469))