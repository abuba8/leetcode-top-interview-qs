class Solution(object):
    def reverse_number(self, n):
        r = 0
        while n>0:
            temp = n % 10
            r = r * 10 + temp
            n = n // 10

        return r

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0: return False
        else:
            temp = self.reverse_number(x)
            if temp == x: return True
            else: return False
        '''
        Alternate solution
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        '''
        
obj = Solution()
print(obj.isPalindrome(-121))